#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""OpenDota webAPI wrapper and parser in Python"""

__author__ = "PeiShang"
__date__ = "11/04/2018"
__version__ = "0.1.1"
__licence__ = "GPL"

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
from urllib import request

import json
from .src import urls
import pandas as pd
import time
import sys
import csv


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
    base_url = urls.GET_PRO_PLAYERS
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


def __get_top_teams(low_lim, up_lim):
    """
    Get data of top teams
    low_lim: low limit of team rank
    up_lim: up limit of team rank
    """
    teams = get_teams()
    top_teams = teams[low_lim:up_lim]
    top_teams_id = [team['team_id'] for team in top_teams]
    top_teams_name = [team['name'] for team in top_teams]
    top_teams_rating = [team['rating'] for team in top_teams]
    top_teams_rating_dic = dict(zip(top_teams_id, top_teams_rating))
    return top_teams_id, top_teams_name, top_teams_rating_dic


def __progressBar(value, endvalue, bar_length=20):
    """print the progress bar"""
    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write("\rPercent: [{0}] {1}% ({2}/{3})".format(arrow + spaces, int(round(percent * 100)), value, endvalue))
    sys.stdout.flush()


def __get_top_team_matches(low_lim, up_lim):
    """get the list of match_id of top teams"""
    print('getting {} to {} teams matches...'.format(low_lim, up_lim))
    top_teams_id, top_teams_name, top_teams_rating_dic = __get_top_teams(low_lim, up_lim)
    matches_lst = []
    team_count = 0
    for team_id in top_teams_id:
        for times in range(10):
            try:
                team_matches = get_team_matches(team_id)
                team_matches_ids = [match['match_id'] for match in team_matches]
                break
            except Exception as e:
                time.sleep(10)
        matches_lst += team_matches_ids
        team_count += 1
        __progressBar(team_count, up_lim - low_lim)
    return list(set(matches_lst)), top_teams_rating_dic


def __get_picks(picks_bans, is_radiant=True):
    picks = []
    if is_radiant:
        team = 0
    else:
        team = 1
    for pick_ban in picks_bans:
        if (pick_ban['is_pick'] == True) and (pick_ban['team'] == team):
            picks.append(pick_ban['hero_id'])
    return picks


def __get_kills_log(players):
    kills_log = []
    for player in players:
        is_radiant = player['isRadiant']
        if is_radiant:
            team = 0 # 0 for radiant 1 for dire
        else:
            team = 1
        k_log = player['kills_log']
        for kill in k_log:
            kills_log.append((team, kill['time']))
    kills_log.sort(key=lambda x: x[1]) # sort by time
    return kills_log


def __get_team_rating(team_id, rating_dict):
    try:
        rating = rating_dict[team_id]
    except:
        rating = 1000 # if not in the top1000 list, set rating to be 1000
    return rating


def __if_radiant_fb(kills_log):
    return kills_log[0][0] == 0


def __if_radiant_10kill(kills_log):
    return kills_log[9][0] == 0


def get_top_team_matches_dataframe(low_lim, up_lim):
    """Generate matches dataframe"""

    matches_id_lst, top_teams_rating_dict = __get_top_team_matches(low_lim, up_lim)
    with open("./matches_lst.csv", "w") as matches_lst_file:
        wr = csv.writer(matches_lst_file)
        for match_id in matches_id_lst:
            wr.writerow(match_id)

    columns = ['Radiant_team_id','Radiant_team_rating', 'Dire_team_id', 'Dire_team_rating',
           'Radiant_hero1', 'Radiant_hero2', 'Radiant_hero3', 'Radiant_hero4', 'Radiant_hero5',
           'Dire_hero1', 'Dire_hero2', 'Dire_hero3', 'Dire_hero4', 'Dire_hero5',
           'Radiant_win', 'Radiant_fb', 'Radiant_10kill', 'start_time']

    count = 0
    df_match_data = pd.DataFrame(columns=columns)
    total_len = len(matches_id_lst)
    print('\nGenerating matches data...')
    for match_id in matches_id_lst:
        for times in range(10):
            try:
                # get data from match data
                match_data = get_match(match_id)

                if match_data['game_mode'] == 2: # if captains mode
                    radiant_win = match_data['radiant_win']
                    radiant_team_id = match_data['radiant_team']['team_id']
                    dire_team_id = match_data['dire_team']['team_id']
                    radiant_team_rating = __get_team_rating(radiant_team_id, top_teams_rating_dict)
                    dire_team_rating = __get_team_rating(dire_team_id, top_teams_rating_dict)

                    picks_bans = match_data['picks_bans']
                    radiant_picks = __get_picks(picks_bans, is_radiant=True)
                    dire_picks = __get_picks(picks_bans, is_radiant=False)

                    players = match_data['players']
                    start_time = match_data['start_time']
                    kills_log = __get_kills_log(players)
                    radiant_fb = __if_radiant_fb(kills_log)
                    radiant_10kill = __if_radiant_10kill(kills_log)
                    df_match_data.loc[count, 'Radiant_team_id'] = radiant_team_id
                    df_match_data.loc[count, 'Radiant_team_rating'] = radiant_team_rating
                    df_match_data.loc[count, 'Dire_team_id'] = dire_team_id
                    df_match_data.loc[count, 'Dire_team_rating'] = dire_team_rating
                    for i in range(5):
                        df_match_data.loc[count, 'Radiant_hero'+str(i+1)] = radiant_picks[i]
                        df_match_data.loc[count, 'Dire_hero'+str(i+1)] = dire_picks[i]
                    df_match_data.loc[count, 'Radiant_win'] = radiant_win
                    df_match_data.loc[count, 'Radiant_fb'] = radiant_fb
                    df_match_data.loc[count, 'Radiant_10kill'] = radiant_10kill
                    df_match_data.loc[count, 'start_time'] = start_time
                    break
            except Exception as e:
                time.sleep(10)
        count += 1
        __progressBar(count, total_len)
    return df_match_data

