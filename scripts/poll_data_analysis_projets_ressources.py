#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:56:44 2024

@author: mndiaye
"""

#%%
"""
### Initialization
"""
import numpy as np
import pandas as pd
import os
from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#%%
"""
### Directories and paths to read files
"""
fdir = Path('/Users/mndiaye/python/rd_poll/data/').resolve()

fname_proj = 'results-survey149427_projets_2024-03-25_cleaned_ressources.xlsx'
fname_labo = 'results-survey966749_labo_2024-03-25_cleaned.xlsx'

fpath_proj = fdir / fname_proj
fpath_labo = fdir / fname_labo

#%%
"""
### Directories and paths to save files
"""
fdir_sav = Path('/Users/mndiaye/python/rd_poll/plots/').resolve()
if not os.path.exists(fdir_sav):
    os.makedirs(fdir_sav)
    

#%%
"""
### Read the file
"""
col_name = [str(x) for x in range(415)]

data_proj_raw = pd.read_excel(fpath_proj, header=0, names=col_name) # dimensions 181x415


#%%
"""
### Select the rows corresponding to the files of the people who went to the final page 
"""
#s2 = data_proj_raw['Dernière page']
# s2 = data_proj_raw['2']
# idx_finalpage = s2 == 8.0

# data_proj = data_proj_raw.loc[idx_finalpage,:]
data_proj = data_proj_raw.loc[:,:]

#%%
"""
### Q5.1 - Ressources humaines totales consacrées au projet de R&D  (colonnes GQ à HF) - 7*26+17-1 (198) à 8*26+6-1 (213)
"""
val = 212

q501_nIni = val
q501_nEnd = val
q501_nPts = q501_nEnd-q501_nIni+1

q501_idx_arr = q501_nIni + np.arange(q501_nPts)

for i in q501_idx_arr:
    
    print(f'column name: {i}')
    q501_lst = data_proj[f'{i}']
    
    unique_q501_lst = q501_lst.unique()
    
    q501_stats  = q501_lst.value_counts()
    
    print(q501_stats)
    print('\n')

   
#%%
"""
### Q5.2 - Ressources humaines totales consacrées au projet de R&D  (colonnes HG) - 8*26+7-1 (214)
"""
val = 214

q502_nIni = val
q502_nEnd = val
q502_nPts = q502_nEnd-q502_nIni+1

q502_idx_arr = q502_nIni + np.arange(q502_nPts)

for i in q502_idx_arr:
    
    print(f'column name: {i}')
    q502_lst = data_proj[f'{i}']
    
    unique_q502_lst = q502_lst.unique()
    
    q502_stats  = q502_lst.value_counts()
    
    print(q502_stats)
    print('\n')
    
    
#%%
"""
### Q5.3 - Sources et montants de financement en k€ du projet (colonnes HH à JG) - 8*26+8-1 (215) à 10*26+7-1 (266)
"""
val = 266

q503_nIni = val
q503_nEnd = val
q503_nPts = q503_nEnd-q503_nIni+1

q503_idx_arr = q503_nIni + np.arange(q503_nPts)

for i in q503_idx_arr:
    
    print(f'column name: {i}')
    q503_lst = data_proj[f'{i}']
    
    unique_q503_lst = q503_lst.unique()
    
    q503_stats  = q503_lst.value_counts()
    
    print(q503_stats)
    print('\n')
    
