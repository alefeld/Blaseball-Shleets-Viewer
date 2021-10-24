import blaseball_mike.database as mikedb
import asyncio
import gspread

import shleets_helper as shelper

credentials = gspread.service_account()
spreadsheet_id = '1rDdGyhxELItkd82vjoN0mLJ9r2GGpeJCeRo33-gb0go'
worksheet = credentials.open_by_key(spreadsheet_id).worksheet('All Data')

async def stream_events(url='https://www.blaseball.com/events/streamData', retry_base=0.01, retry_max=300):
    from concurrent import futures
    import ujson

    from aiohttp_sse_client import client as sse_client
    from aiohttp.client_exceptions import ClientPayloadError, ClientConnectorError, ServerDisconnectedError
    """
    Async generator for the events API.
    `retry_base` will be the minimum time to delay if there's a connection error
    `retry_max` is the maximum time to delay if there's a connection error
    """
    retry_delay = retry_base
    event_last = None
    sim_last = None
    while True:
        try:
            async with sse_client.EventSource(url, read_bufsize=2 ** 18, timeout=-1) as src:
                async for event in src:
                    retry_delay = retry_base  # reset backoff
                    if not event.data:
                        continue
                    try:
                        payload = ujson.loads(event.data)['value']
                        event_last = payload
                        sim_tmp = payload.get('games',{}).get('sim',{})
                        if sim_tmp:
                            sim_last = sim_tmp
                    except: # Debug, but it's been tested and everything should be fine.
                        print("Something bad happened")
                        print(event_last)
                        print(sim_last)
                        print(event.data)
                    if payload.get('games',{}).get('sim',{}).get('phase',0) in [3,5,10,12,14]: # This timestamp expires at earlsiesta, latesiesta, end of early postseason, end of latepostseason, (and at semi-centennial)
                        return
                    yield payload

        except (ConnectionError,
                TimeoutError,
                ClientPayloadError,
                futures.TimeoutError,
                asyncio.exceptions.TimeoutError,
                ClientConnectorError,
                ServerDisconnectedError) as error:
            await asyncio.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, retry_max)


async def main():
    # Main script

    # Initialize variables
    today = -1
    innings_away = [['','','','','','','','',''] for ngames in range(12)]
    innings_home = [['','','','','','','','',''] for ngames in range(12)]
    games_map = {}
    teams = None
    players = []
    player_ids_cache = set()
    counter_playerget = 0

    # Get data stream and process it constantly
    for timestamp in shelper.timestamps_expansion:
        print(timestamp)
        event_stream = stream_events(url=timestamp)
        async for event in event_stream:
            if event.get('games',{}).get('schedule'):
                # Get team lineups
                if event.get('leagues'):
                    teams = event.get('leagues',{}).get('teams')
                if not teams:
                    continue
                teams = [team for team in teams if team['id'] in shelper.team_map.keys()] # Remove teams not playing
                player_ids = [player for team in teams for player in team['lineup']]
                if (set(player_ids) != player_ids_cache) or (counter_playerget >= 100):
                    players = mikedb.get_player(player_ids)
                    player_ids_cache = set(player_ids)
                    counter_playerget = 0
                counter_playerget += 1
                player_map = {} # Used later as well
                for player in players.values():
                    player_map[player['id']] = player.get('unscatteredName',player.get('name'))
                team_lineups = {}
                for team in teams:
                    lineup = team['lineup']
                    lineup_names = [player_map[player] for player in lineup]
                    while len(lineup_names) < 16:
                        lineup_names.append('')
                    team_lineups[team['id']] = lineup_names

                # Initialize bulk data structures
                payload_dict = {}
                weathers = ['' for ngames in range(12)]
                feeds = ['' for ngames in range(12)]
                feed_types = [0 for ngames in range(12)]
                away_ids = ['' for ngames in range(12)]
                home_ids = ['' for ngames in range(12)]
                base5s = ['' for ngames in range(12)]
                balls_all = ['' for ngames in range(12)]
                strikes_all = ['' for ngames in range(12)]
                outs_all = ['' for ngames in range(12)]
                finalized_all = ['' for ngames in range(12)]
                battings = ['' for ngames in range(12)]
                away_scores = ['' for ngames in range(12)]
                home_scores = ['' for ngames in range(12)]

                # Get games
                games = event['games']['schedule']
                # Reset inning scores and set a new fixed order of games if it's a new day
                if event['games']['sim']['day'] != today:
                    innings_away = [['','','','','','','','',''] for ngames in range(12)]
                    innings_home = [['','','','','','','','',''] for ngames in range(12)]
                    today = event['games']['sim']['day']
                    games_map = {}
                    for i_game,game in enumerate(games):
                        games_map[game['id']] = i_game

                # Loop over games
                for game in games:
                    i_game = games_map[game['id']]

                    # Get baserunners
                    bases = game['basesOccupied']
                    baserunners = game['baseRunners']
                    baserunner_names = [player_map.get(baserunner,'A GHOST!') for baserunner in baserunners]
                    bases_all = ['','','','']
                    for base,baserunner_name in zip(bases,baserunner_names):
                        if base <= 3: # Prevents problems with bases beyond the fifth base.
                            bases_all[base] = baserunner_name
                    if game['topOfInning']:
                        away_baserunners = bases_all
                        home_baserunners = ['','','','']
                    else:
                        home_baserunners = bases_all
                        away_baserunners = ['','','','']
                    # Get home team
                    home_bases = home_baserunners
                    home_id = game['homeTeam']
                    home_ids[i_game] = home_id
                    home_pitcher = game['homePitcherName']
                    home_batter = player_map.get(game['homeBatter'],'') if not game['topOfInning'] else ''
                    # Get away team
                    away_bases = away_baserunners
                    away_id = game['awayTeam']
                    away_ids[i_game] = away_id
                    away_pitcher = game['awayPitcherName']
                    away_batter = player_map.get(game['awayBatter'],'') if game['topOfInning'] else ''
                    # Add to payload
                    payload_dict[shelper.team_map[home_id]] = [home_pitcher]+[home_batter]+home_bases+team_lineups[home_id]
                    payload_dict[shelper.team_map[away_id]] = [away_pitcher]+[away_batter]+away_bases+team_lineups[away_id]

                    # Get game data
                    if game['topOfInning']:
                        batting = away_id
                        if game['inning'] in range(9):
                            innings_away[i_game][game['inning']] = game['awayScore'] - sum([innings_away[i_game][inning] for inning in range(game['inning']) if innings_away[i_game][inning] != '']) #game['halfInningScore'] # halfInning* fields are bugged for home team =/
                    else:
                        batting = home_id
                        if game['inning'] in range(9):
                            innings_home[i_game][game['inning']] = game['homeScore'] - sum([innings_home[i_game][inning] for inning in range(game['inning']) if innings_home[i_game][inning] != '']) #game['halfInningScore'] # halfInning* fields are bugged for home team =/
                    weathers[i_game] = game['weather']
                    feeds[i_game] = game['lastUpdate'].replace('\n',' ')
                    feed_types[i_game] = shelper.feedtyper(game['lastUpdate'])
                    base5s[i_game] = True if game['homeBases']==5 else False
                    balls_all[i_game] = game['atBatBalls']
                    strikes_all[i_game] = game['atBatStrikes']
                    outs_all[i_game] = game['halfInningOuts']
                    finalized_all[i_game] = game['finalized']
                    battings[i_game] = batting
                    away_scores[i_game] = game['awayScore']
                    home_scores[i_game] = game['homeScore']

                # Assemble all data for this tick
                payload = []
                for row in range(1,25):
                    payload.append(payload_dict.get(row,['']))
                payload.append([event.get('games').get('sim').get('season')+1,event.get('games').get('sim').get('day')+1,'','','','','','','','','',''])
                payload.append(weathers)
                payload.append(feeds)
                payload.append(feed_types)
                payload.append(away_ids)
                payload.append(home_ids)
                payload.append(base5s)
                payload.append(balls_all)
                payload.append(strikes_all)
                payload.append(outs_all)
                payload.append(finalized_all)
                payload.append(battings)
                payload.append(away_scores)
                payload.append(home_scores)
                for inning in range(9):
                    payload.append([game[inning] for game in innings_away])
                for inning in range(9):
                    payload.append([game[inning] for game in innings_home])
                # Upload Sheets with this tick
                worksheet.update('G2:AB57', payload)


# Execution starts here.
while True:
    asyncio.run(main())