#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The base URL and the API calls are defined in this file"""

GET_MATCHE = 'https://api.opendota.com/api/matches/{match_id}'

GET_PLAYER = 'https://api.opendota.com/api/players/{account_id}'
GET_PLAYER_WL = 'https://api.opendota.com/api/players/{account_id}/wl'
GET_PLAYER_RECENT_MATCHES = 'https://api.opendota.com/api/players/{account_id}/recentMatches'
GET_PLAYER_MATCHES_PLAYED = 'https://api.opendota.com/api/players/{account_id}/matches'
GET_PLAYER_HEROES_PLAYED = 'https://api.opendota.com/api/players/{account_id}/heroes'
GET_PLAYER_PEERS = 'https://api.opendota.com/api/players/{account_id}/peers'
GET_PLAYER_PRO_PEERS = 'https://api.opendota.com/api/players/{account_id}/pros'
GET_PLAYER_TOTAL_STARS = 'https://api.opendota.com/api/players/{account_id}/totals'
GET_PLAYER_CATEGORY_COUNTS = 'https://api.opendota.com/api/players/{account_id}/counts'
GET_PLAYER_HISTOGRAMS = 'https://api.opendota.com/api/players/{account_id}/histograms/{field}'
GET_PLAYER_WARDMAP = 'https://api.opendota.com/api/players/{account_id}/wardmap'
GET_PLAYER_WORDCLOUD = 'https://api.opendota.com/api/players/{account_id}/wordcloud'
GET_PLAYER_RATINGS = 'https://api.opendota.com/api/players/{account_id}/ratings'
GET_PLAYER_HERO_RANKINGS = 'https://api.opendota.com/api/players/{account_id}/rankings'
POST_PLAYER_REFRESH = 'https://api.opendota.com/api/players/{account_id}/refresh'

GET_PRO_PLAYERS = 'https://api.opendota.com/api/proPlayers'
GET_PRO_MATCHES = 'https://api.opendota.com/api/proMatches'
GET_PUBLIC_MATCHES = 'https://api.opendota.com/api/publicMatches'
GET_SQL_QUERIES = 'https://api.opendota.com/api/explorer'
GET_MMR_DISTRIBUTIONS = 'https://api.opendota.com/api/distributions'
GET_PLAYERS_BY_NAME = 'https://api.opendota.com/api/search'
GET_TOP_PLATERS_BY_HERO = 'https://api.opendota.com/api/rankings'
GET_HERO_BENCHMARKS = 'https://api.opendota.com/api/benchmarks'
GET_SERVICE_STATUS = 'https://api.opendota.com/api/status'

GET_HEROES = 'https://api.opendota.com/api/heroes'
GET_MATCHES_BY_HERO = 'https://api.opendota.com/api/heroes/{hero_id}/matches'
GET_HERO_MATCHUPS = 'https://api.opendota.com/api/heroes/{hero_id}/matchups'
GET_HERO_WINS_BY_DURATION = 'https://api.opendota.com/api/heroes/{hero_id}/durations'
GET_HERO_PLAYERS = 'https://api.opendota.com/api/heroes/{hero_id}/players'
GET_HERO_STATS = 'https://api.opendota.com/api/heroStats'

GET_LEAGUES = 'https://api.opendota.com/api/leagues'
GET_TEAMS = 'https://api.opendota.com/api/teams'
GET_TEAM = 'https://api.opendota.com/api/teams/{team_id}'
GET_TEAM_MATCHES = 'https://api.opendota.com/api/teams/{team_id}/matches'
GET_TEAM_PLAYERS = 'https://api.opendota.com/api/teams/{team_id}/players'
GET_TEAM_HEROES = 'https://api.opendota.com/api/teams/{team_id}/heroes'

GET_REPLAYS = 'https://api.opendota.com/api/replays'
GET_TOP_PERFORMANCES = 'https://api.opendota.com/api/records/{field}'
GET_TOP_LIVE = 'https://api.opendota.com/api/live'

GET_SCENARIOS_ITEM_TIMINGS = 'https://api.opendota.com/api/scenarios/itemTimings'
GET_SCENARIOS_LANE_ROLES = 'https://api.opendota.com/api/scenarios/laneRoles'
GET_SCENARIOS_MISC = 'https://api.opendota.com/api/scenarios/misc'

GET_DATABASE_SCHEMA = 'https://api.opendota.com/api/schema'
