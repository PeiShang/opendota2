#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Test the api'''
import opendota2 as op

# get top 10 team matches
matches_df = op.get_top_team_matches_dataframe(0, 2)
