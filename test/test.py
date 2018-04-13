#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Test the api'''
import opendota2 as op
import pandas as pd

# get top 1000 team matches
matches_df = op.get_top_team_matches_dataframe(0, 1000)
matches_df.to_csv('Top_1000_teams_matches.csv')
