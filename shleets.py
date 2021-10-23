import blaseball_mike.database as mikedb
import asyncio
import gspread


credentials = gspread.service_account()
spreadsheet_id = '1rDdGyhxELItkd82vjoN0mLJ9r2GGpeJCeRo33-gb0go'
worksheet = credentials.open_by_key(spreadsheet_id).worksheet('All Data')

timestamps = [
    'https://api.sibr.dev/replay/v1/replay?from=2021-03-01T15:59:50.17Z&interval=4000', # Season 12 earlseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-03-02T19:59:50.17Z&interval=4000', # Season 12 midseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-03-04T18:59:50.17Z&interval=4000', # Season 12 lateseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-03-06T15:59:50.17Z&interval=4000', # Season 12 semifinals
    'https://api.sibr.dev/replay/v1/replay?from=2021-03-08T15:59:50.17Z&interval=4000', # Season 13 earlseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-03-09T19:59:50.17Z&interval=4000', # Season 13 midseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-03-11T18:59:50.17Z&interval=4000', # Season 13 lateseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-03-13T15:59:50.17Z&interval=4000', # Season 13 semifinals
    'https://api.sibr.dev/replay/v1/replay?from=2021-03-15T15:59:50.17Z&interval=4000', # Season 14 earlseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-03-16T19:59:50.17Z&interval=4000', # Season 14 midseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-03-18T18:59:50.17Z&interval=4000', # Season 14 lateseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-03-20T15:59:50.17Z&interval=4000', # Season 14 semifinals
    'https://api.sibr.dev/replay/v1/replay?from=2021-04-05T15:59:50.17Z&interval=4000', # Season 15 earlseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-04-06T19:59:50.17Z&interval=4000', # Season 15 midseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-04-08T18:59:50.17Z&interval=4000', # Season 15 lateseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-04-10T15:59:50.17Z&interval=4000', # Season 15 semifinals
    'https://api.sibr.dev/replay/v1/replay?from=2021-04-12T15:59:50.17Z&interval=4000', # Season 16 earlseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-04-13T20:59:50.17Z&interval=4000', # Season 16 midseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-04-15T20:59:50.17Z&interval=4000', # Season 16 lateseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-04-17T15:59:50.17Z&interval=4000', # Season 16 semifinals
    'https://api.sibr.dev/replay/v1/replay?from=2021-04-19T15:59:50.17Z&interval=4000', # Season 17 earlseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-04-20T19:59:50.17Z&interval=4000', # Season 17 midseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-04-22T18:59:50.17Z&interval=4000', # Season 17 lateseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-04-24T15:59:50.17Z&interval=4000', # Season 17 semifinals
    'https://api.sibr.dev/replay/v1/replay?from=2021-05-10T15:59:50.17Z&interval=4000', # Season 18 earlseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-05-11T20:59:50.17Z&interval=4000', # Season 18 midseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-05-13T19:59:50.17Z&interval=4000', # Season 18 lateseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-05-15T15:59:50.17Z&interval=4000', # Season 18 semifinals
    'https://api.sibr.dev/replay/v1/replay?from=2021-05-17T15:59:50.17Z&interval=4000', # Season 19 earlseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-05-18T19:59:50.17Z&interval=4000', # Season 19 midseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-05-20T15:59:50.17Z&interval=4000', # Season 19 lateseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-05-22T15:59:50.17Z&interval=4000', # Season 19 semifinals
    'https://api.sibr.dev/replay/v1/replay?from=2021-06-14T15:59:50.17Z&interval=4000', # Season 20 earlseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-06-15T19:59:50.17Z&interval=4000', # Season 20 midseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-06-17T18:59:50.17Z&interval=4000', # Season 20 lateseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-06-19T15:59:50.17Z&interval=4000', # Season 20 semifinals
    'https://api.sibr.dev/replay/v1/replay?from=2021-06-21T15:59:50.17Z&interval=4000', # Season 21 earlseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-06-22T19:59:50.17Z&interval=4000', # Season 21 midseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-06-24T18:59:50.17Z&interval=4000', # Season 21 lateseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-06-26T15:59:50.17Z&interval=4000', # Season 21 semifinals
    'https://api.sibr.dev/replay/v1/replay?from=2021-06-28T15:59:50.17Z&interval=4000', # Season 22 earlseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-06-29T19:59:50.17Z&interval=4000', # Season 22 midseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-07-01T19:59:50.17Z&interval=4000', # Season 22 lateseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-07-03T15:59:50.17Z&interval=4000', # Season 22 semifinals
    'https://api.sibr.dev/replay/v1/replay?from=2021-07-19T15:59:50.17Z&interval=4000', # Season 23 earlseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-07-20T19:59:50.17Z&interval=4000', # Season 23 midseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-07-22T18:59:50.17Z&interval=4000', # Season 23 lateseason
    'https://api.sibr.dev/replay/v1/replay?from=2021-07-24T15:59:50.17Z&interval=4000', # Season 23 semifinals
]

team_map = {
    '747b8e4a-7e50-4638-a973-ea7950a3e739': 1,
    'a37f9158-7f82-46bc-908c-c9e2dda7c33b': 2,
    'ca3f1c8c-c025-4d8e-8eef-5be6accbeb16': 3,
    '57ec08cc-0411-4643-b304-0e80dbc15ac7': 4,
    'c73b705c-40ad-4633-a6ed-d357ee2e2bcf': 5,
    'd9f89a8a-c563-493e-9d64-78e4f9a55d4a': 6,
    'f02aeae2-5e6a-4098-9842-02d2273f25c7': 7,
    '9debc64f-74b7-4ae1-a4d6-fce0144b6ea5': 8,
    'b63be8c2-576a-4d6e-8daf-814f8bcea96f': 9,
    '3f8bbb15-61c0-4e3f-8e4a-907a5fb1565e': 10,
    '878c1bf6-0d21-4659-bfee-916c8314d69c': 11,
    'bb4a9de5-c924-4923-a0cb-9d1445f1ee5d': 12,
    '23e4cbc1-e9cd-47fa-a35b-bfa06f726cb7': 13,
    '105bc3ff-1320-4e37-8ef0-8d595cb95dd0': 14,
    '36569151-a2fb-43c1-9df7-2df512424c82': 15,
    'b72f3061-f573-40d7-832a-5ad475bd7909': 16,
    'b024e975-1c4a-4575-8936-a3754a08806a': 17,
    '46358869-dce9-4a01-bfba-ac24fc56f57e': 18,
    '979aee4a-6d80-4863-bf1c-ee1a78e06024': 19,
    'eb67ae5e-c4bf-46ca-bbbc-425cd34182ff': 20,
    'adc5b394-8f76-416d-9ce9-813706877b84': 21,
    '7966eb04-efcc-499b-8f03-d13916330531': 22,
    'bfd38797-8404-4b38-8b82-341da28b1f83': 23,
    '8d87c468-699a-47a8-b40d-cfb73a5660ad': 24,
}
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


def feedtyper(event):
    # Function for reverse-engineering feed type
    event_lower = event.lower()
    type = 0

    if 'runs are overflowing' in event_lower:
        type = 20
    elif 'apply home field advantage' in event_lower:
        type = 21
    elif 'with a pitch' in event_lower:
        type = 22
    elif 'shelled and cannot escape' in event_lower:
        type = 23
    elif 'is partying' in event_lower:
        type = 24
    elif 'the electricity zaps a strike away!' == event_lower:
        type = 25
    elif 'mild pitch' in event_lower:
        type = 27
    elif 'the black hole swallow' in event_lower:
        type = 30
    elif 'sun 2 smiled' in event_lower:
        type = 31
    elif 'the birds circle ... but they don\'t find what they\'re looking for' in event_lower:
        type = 33
    elif 'a murder of crows ambush' in event_lower:
        type = 34
    elif 'the birds circle ... the birds pecked' in event_lower:
        type = 35
    elif 'triple threat' in event_lower:
        type = 36
    elif 'got a free refill' in event_lower:
        type = 37
    elif 'is wired!' in event_lower:
        type = '39a'
    elif 'is tired.' in event_lower:
        type = '39b'
    elif 'is tangled in the flicker' in event_lower:
        type = 40
    elif 'reality flickers.' in event_lower:
        type = 41
    elif 'superallergic reaction' in event_lower:
        type = 45
    elif 'an allergic reaction' in event_lower:
        type = 47
    elif 'reverberations' in event_lower:
        type = 48
    elif 'siphoned some' in event_lower:
        type = 51
    elif 'tried to siphon blood' in event_lower:
        type = 53
    elif 'rogue umpire incinerated' in event_lower:
        type = 54
    elif 'rogue umpire tried to incinerate' in event_lower:
        type = 55
    elif 'a surge of immateria rushes up from under' in event_lower:
        type = 62
    elif 'the salmon swim upstream' in event_lower:
        type = 63
    elif 'secret base' in event_lower:
        type = 65
    elif 'consumer' in event_lower:
        type = 67
    elif 'echo chamber' in event_lower:
        type = 69
    elif 'grind rail' in event_lower:
        type = 70
    elif 'entered the tunnels' in event_lower:
        type = 71
    elif 'peanut mister activates' in event_lower:
        type = 72
    elif 'tastes the infinite' in event_lower:
        type = 74
    elif 'the event horizon' in event_lower:
        type = 76
    elif 'the solar panels are angled toward sun 2.' == event_lower:
        type = 78
    elif 'solar panels absorb' in event_lower:
        type = 79
    elif 'elsewhere' in event_lower: # must be after flooding
        type = 84
    elif ', over under,' in event_lower:
        type = 85
    elif ', under over,' in event_lower:
        type = 86
    elif 'the atlantis georgias go undersea. they\'re now overperforming!' == event_lower:
        type = 88
    elif 'happy to be home' in event_lower:
        type = 91
    elif 'homesick' in event_lower:
        type = 91
    elif 'perks up' in event_lower:
        type = 93
    elif 'earlbird' in event_lower:
        type = 96
    elif 'late to the party' in event_lower:
        type = 97
    elif 'shame donations are granted' in event_lower:
        type = 99
    elif 'shuffled in the reverb' in event_lower: # must be after 48,49
        type = 130
    elif 'had their lineup shuffled' in event_lower: # must be after 49
        type = 131
    elif 'the pressure is' in event_lower:
        type = 165
    elif 'echoed' in event_lower:
        type = 169
    elif 'static echo' in event_lower:
        type = 170
    elif 'psychoacoustics echo' in event_lower:
        type = 173
    elif 'a shimmering crate descends' in event_lower:
        type = 177
    elif 'middling' in event_lower:
        type = 178
    elif 'enters the crime scene' in event_lower:
        type = 181
    elif 'the community chest opens' in event_lower:
        type = 189
    elif 'incoming shadow fax' in event_lower:
        type = 191
    elif 'hotel motel' in event_lower:
        type = 192
    elif 'prize match!' in event_lower:
        type = 193
    elif 'smithy beckons to' in event_lower:
        type = 195
    elif 'have a blood type' in event_lower:
        type = 198
    elif 'hype built in' in event_lower:
        type = 206
    elif 'practice moderation' in event_lower:
        type = 208
    elif 'black hole (black hole) nullified' in event_lower:
        type = 211
    elif 'sun(sun)\'s pressure built...' in event_lower:
        type = 217
    elif 'sun 30 smiled upon them.' in event_lower:
        type = 226
    elif 'home team shutout. incoming voicemail...' in event_lower:
        type = 228
    elif 'thieves\' guild convened. they stole' in event_lower:
        type = 230
    elif 'reloaded all of the bases' in event_lower:
        type = 239
    elif 'sun(sun) supernova' in event_lower:
        type = 247
    elif 'a riff opened.' in event_lower:
        type = 251
    elif 'night shift. a deep darkness took' in event_lower:
        type = 252
    elif 'became stuck!' in event_lower:
        type = 254
    elif 'horse power achieved' in event_lower:
        type = 255
    return type
    

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
    for timestamp in timestamps:
        print(timestamp)
        event_stream = stream_events(url=timestamp)
        async for event in event_stream:
        # async for event in stream_events(url='https://api.sibr.dev/replay/v1/replay?from=2021-06-16T00:59:50.17Z&interval=1500'): # Faster
        # async for event in stream_events(url='https://api.sibr.dev/replay/v1/replay?from=2021-03-01T15:59:50.17Z&interval=4000'):
        # async for event in stream_events(url='https://api.sibr.dev/replay/v1/replay?from=2021-07-30T15:59:50.17Z&interval=4000'):
        # async for event in stream_events(url='https://api.sibr.dev/replay/v1/replay?from=2021-06-16T00:59:50.17Z&interval=4000'): # Normal?
        # async for event in stream_events(url='https://api.sibr.dev/replay/v1/replay?from=2020-10-05T16:31:50.17Z&interval=1500'): # Crowvertime
        # async for event in stream_events(url='https://api.sibr.dev/replay/v1/replay?from=2021-05-20T11:44:50.17Z&interval=1500'): # Drumsolo
            if event.get('games',{}).get('schedule'):
                # Get team lineups
                if event.get('leagues'):
                    teams = event.get('leagues',{}).get('teams')
                if not teams:
                    continue
                teams = [team for team in teams if team['id'] in team_map.keys()] # Remove teams not playing
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
                    payload_dict[team_map[home_id]] = [home_pitcher]+[home_batter]+home_bases+team_lineups[home_id]
                    payload_dict[team_map[away_id]] = [away_pitcher]+[away_batter]+away_bases+team_lineups[away_id]

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
                    feed_types[i_game] = feedtyper(game['lastUpdate'])
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