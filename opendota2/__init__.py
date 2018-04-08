#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""OpenDota webAPI wrapper and parser in Python"""

__author__ = "PeiShang"
__date__ = "01/04/2018"
__version__ = "1.0"
__licence__ = "GPL"

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
from urllib import request

import json
from .src import urls

def __build_url(base_url, **kwargs):
    api_query = urlencode(kwargs)
    return '{0}?{1}'.format(base_url, api_query)

def get_match(match_id):
    """Match data"""
    base_url = urls.GET_MATCHE.replace("{match_id}", str(match_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_player(account_id):
    """Player data"""
    base_url = urls.GET_PLAYER.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json


def get_player_wl(account_id, **kwargs):
    """Player win/lost count """
    base_url = urls.GET_PLAYER_WL.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_player_recent_matches(account_id):
    """Player recent matches played """
    base_url = urls.GET_PLAYER_RECENT_MATCHES.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_player_matches_played(account_id, **kwargs):
    """Player matches played """
    base_url = urls.GET_PLAYER_MATCHES_PLAYED.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_player_heroes_played(account_id, **kwargs):
    """Player heroes played """
    base_url = urls.GET_PLAYER_HEROES_PLAYED.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_player_peers(account_id, **kwargs):
    """Players played with"""
    base_url = urls.GET_PLAYER_PEERS.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json


def get_player_pro_peers(account_id, **kwargs):
    """Pro players played with"""
    base_url = urls.GET_PLAYER_PRO_PEERS.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_player_total_stars(account_id, **kwargs):
    """Total in stars"""
    base_url = urls.GET_PLAYER_TOTAL_STARS.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_player_category_counts(account_id, **kwargs):
    """Counts in categories"""
    base_url = urls.GET_PLAYER_CATEGORY_COUNTS.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_player_histograms(account_id, **kwargs):
    """Distribution of matches in a single stat"""
    base_url = urls.GET_PLAYER_HISTOGRAMS.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_player_wardmap(account_id, **kwargs):
    """Wards placed in matches played"""
    base_url = urls.GET_PLAYER_WARDMAP.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_player_wordcloud(account_id, **kwargs):
    """Words said/read in matches played"""
    base_url = urls.GET_PLAYER_WORDCLOUD.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_player_ratings(account_id):
    """Player rating history"""
    base_url = urls.GET_PLAYER_RATINGS.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_player_rankings(account_id):
    """Player hero rankings"""
    base_url = urls.GET_PLAYER_RANKINGS.replace("{account_id}", str(account_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_pro_players():
    """Get list of pro players"""
    base_url = urls.GET_PRO_PLAYER
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_pro_matches():
    """Get list of pro matches"""
    base_url = urls.GET_PRO_MATCHES
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_public_matches(**kwargs):
    """Get list of randomly sampled public matches"""
    base_url = urls.GET_PUBLIC_MATCHES
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_sql_queries(**kwargs):
    """Submit arbitrary SQL queries to the database"""
    base_url = urls.GET_SQL_QUERIES
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None

def get_mmr_distributions():
    """Submit arbitrary SQL queries to the database"""
    base_url = urls.GET_MMR_DISTRIBUTIONS
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None

def get_players_by_name(**kwargs):
    """Search players by person name"""
    base_url = urls.GET_PLAYERS_BY_NAME
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_top_players_by_hero(**kwargs):
    """Top players by hero"""
    base_url = urls.GET_TOP_PLAYERS_BY_HERO
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_hero_benchmarks(**kwargs):
    """Benchmarks of average stat values for a hero"""
    base_url = urls.GET_HERO_BENCHMARKS
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_service_status():
    """Get current service statistics"""
    base_url = urls.GET_SERVICE_STATUS
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_heroes():
    """Get hero data"""
    base_url = urls.GET_HEROES
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_matches_by_hero(hero_id):
    """Get recent matches with a hero"""
    base_url = urls.GET_MATCHES_BY_HERO.replace("{hero_id}", str(hero_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_hero_matchups(hero_id):
    """Get results against other heros for a hero"""
    base_url = urls.GET_HERO_MATCHUPS.replace("{hero_id}", str(hero_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_hero_wins_by_duration(hero_id):
    """Get hero performance over a range of match duration"""
    base_url = urls.GET_HERO_WINS_BY_DURATION.replace("{hero_id}", str(hero_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_hero_players(hero_id):
    """Get players who have played this hero"""
    base_url = urls.GET_HERO_PLAYERS.replace("{hero_id}", str(hero_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_hero_stats(hero_id):
    """Get stats about hero performance in recent matches"""
    base_url = urls.GET_HERO_STATS.replace("{hero_id}", str(hero_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_leagues():
    """Get league data"""
    base_url = urls.GET_LEAGUES
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_teams():
    """Get team data"""
    base_url = urls.GET_TEAMS
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_team(team_id):
    """Get data for a team"""
    base_url = urls.GET_TEAM.replace("{team_id}", str(team_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_team_matches(team_id):
    """Get matches for a team"""
    base_url = urls.GET_TEAM_MATCHES.replace("{team_id}", str(team_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_team_players(team_id):
    """Get players who have played for a team"""
    base_url = urls.GET_TEAM_PLAYERS.replace("{team_id}", str(team_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_team_heroes(team_id):
    """Get heroes for a team"""
    base_url = urls.GET_TEAM_HEORES.replace("{team_id}", str(team_id))
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_replays(**kwargs):
    """Get data to construct a replay URL with"""
    base_url = urls.GET_REPLAYS
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_top_performances(**kwargs):
    """Get top performances in a stat"""
    base_url = urls.GET_TOP_PERFORMANCES
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_top_live():
    """Get top currently ongoing live games"""
    base_url = urls.GET_TOP_LIVE
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_scenarios_item_timings(**kwargs):
    """Win rate for certain item timings on a hero for items that cost at least 2000 gold"""
    base_url = urls.GET_SCENARIOS_ITEMTIMINGS
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_scenarios_lane_roles(**kwargs):
    """Win rate for heroes in certain lane roles"""
    base_url = urls.GET_SCENARIOS_LANE_ROLES 
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_scenarios_misc(**kwargs):
    """Miscellaneous team scenarios"""
    base_url = urls.GET_SCENARIOS_MISC 
    full_url = __build_url(base_url, **kwargs)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

def get_database_schema():
    """Get database schema"""
    base_url = urls.GET_DATABASE_SCHEMA 
    full_url = __build_url(base_url)
    try:
    	data = request.urlopen(full_url).read()
    	data_json = json.loads(data.decode('utf-8'))
    except:
    	data_json = None
    return data_json

