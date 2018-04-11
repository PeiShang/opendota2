#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Test the api'''
import opendota2 as op

match_data = op.get_match(3826321576)
game_mode = match_data['game_mode']
matches_df = op.get_top_team_matches_dataframe(100)
print(top_matches)
