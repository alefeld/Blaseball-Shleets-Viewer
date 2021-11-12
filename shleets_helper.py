# A module of functions and  for Shleets

timestamps_expansion = [
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

# team_map = { # Expansion Era
#     '747b8e4a-7e50-4638-a973-ea7950a3e739': 1,
#     'a37f9158-7f82-46bc-908c-c9e2dda7c33b': 2,
#     'ca3f1c8c-c025-4d8e-8eef-5be6accbeb16': 3,
#     '57ec08cc-0411-4643-b304-0e80dbc15ac7': 4,
#     'c73b705c-40ad-4633-a6ed-d357ee2e2bcf': 5,
#     'd9f89a8a-c563-493e-9d64-78e4f9a55d4a': 6,
#     'f02aeae2-5e6a-4098-9842-02d2273f25c7': 7,
#     '9debc64f-74b7-4ae1-a4d6-fce0144b6ea5': 8,
#     'b63be8c2-576a-4d6e-8daf-814f8bcea96f': 9,
#     '3f8bbb15-61c0-4e3f-8e4a-907a5fb1565e': 10,
#     '878c1bf6-0d21-4659-bfee-916c8314d69c': 11,
#     'bb4a9de5-c924-4923-a0cb-9d1445f1ee5d': 12,
#     '23e4cbc1-e9cd-47fa-a35b-bfa06f726cb7': 13,
#     '105bc3ff-1320-4e37-8ef0-8d595cb95dd0': 14,
#     '36569151-a2fb-43c1-9df7-2df512424c82': 15,
#     'b72f3061-f573-40d7-832a-5ad475bd7909': 16,
#     'b024e975-1c4a-4575-8936-a3754a08806a': 17,
#     '46358869-dce9-4a01-bfba-ac24fc56f57e': 18,
#     '979aee4a-6d80-4863-bf1c-ee1a78e06024': 19,
#     'eb67ae5e-c4bf-46ca-bbbc-425cd34182ff': 20,
#     'adc5b394-8f76-416d-9ce9-813706877b84': 21,
#     '7966eb04-efcc-499b-8f03-d13916330531': 22,
#     'bfd38797-8404-4b38-8b82-341da28b1f83': 23,
#     '8d87c468-699a-47a8-b40d-cfb73a5660ad': 24,
# }

team_map = { # Short Circuits
    '86f4485a-a6db-470b-82f5-e95e6b353537': 1,
    'd82a1a80-dff3-4767-bab6-484b2eb7aee1': 2,
    '16d1fd9b-c62b-4bed-b68a-b3a2d6e21524': 3,
    '23a2cea4-5df7-4ed0-bb2c-b8c297518ada': 4,
    '8d7ba290-5f87-403c-81e3-cf5a2b6a6082': 5,
    '44d9dc46-7e81-4e21-acff-c0f5dd399ae3': 6,
    '57d3f614-f8d3-4dfd-b486-075f823fdb0b': 7,
    '6526d5df-6a9c-48e1-ba50-12dec0d8b22f': 8,
    '89796ffb-843a-4163-8dec-1bef229c68cb': 9,
    '93e71a0e-80fc-46b7-beaf-d204c425fe03': 10,
    '2957236a-6077-4012-a445-8c5be111afd0': 11,
    '74aea6b6-34f9-48f4-b298-7345e1f9f7cb': 12,
    '76d3489f-c7c4-4cb9-9c58-b1e1bab062d1': 13,
    '2dc7a1fa-3ae6-47ed-8c92-5d80167959f5': 14,
    'b069fdc6-2204-423a-932c-09037adcd845': 15,
    'b320131f-da0d-43e1-9b98-f936a0ee417a': 16,
    '0b672007-ebfb-476d-8fdb-fb66bad78df2': 17,
    'e11df0cc-3a95-4159-9a84-fecbbf23ae05': 18,
    'effdbd8d-a54f-4049-a3c8-b5f944e5278b': 19,
    '8981c839-cbcf-47e3-a74e-8731dcff24fe': 20,
    'b7df2ea6-f4e8-4e6b-8c98-f730701f3717': 21,
    'a01f0ade-0186-464d-8c68-e19a29cb66f0': 22,
    '75667373-b350-499b-b86e-5518b6f9f6ab': 23,
    'b35926d4-22a3-4419-8fab-686c41687055': 24,
}

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