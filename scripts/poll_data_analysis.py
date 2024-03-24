#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:39:09 2024

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
### Directories and paths
"""
fdir = Path('/Users/mndiaye/python/rd_poll/data/').resolve()

fname_proj = 'results-survey149427_projets_2024-03-21_v2.xlsx'
fname_labo = 'results-survey966749_labo_2024-03-21.xlsx'

fpath_proj = fdir / fname_proj
fpath_labo = fdir / fname_labo

#%%
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
s2 = data_proj_raw['2']
idx_finalpage = s2 == 8.0

data_proj = data_proj_raw.loc[idx_finalpage,:]

#%%
"""
### Liste de laboratoires
"""
labos_lst = data_proj['5']

uniquelabos_lst = labos_lst.unique()

test  = labos_lst.value_counts()

#%%
"""
### Personnel ayant répondu
"""
personnel_lst = data_proj['7']

uniquepersonnel_lst = personnel_lst.unique()

test2  = personnel_lst.value_counts()

#%%
"""
### Genre de la personne ayant répondu
"""
gender_lst = data_proj['9']

uniquegender_lst = gender_lst.unique()

gender_test = gender_lst.value_counts()

#%%
"""
### Age de la personne ayant répondu
"""
age_lst = data_proj['10']

uniqueage_lst = age_lst.unique()

age_test = age_lst.value_counts()

#%%
"""
### Connaissance formation pour la personne ayant répondu
"""
training_lst = data_proj['11']

uniquetraining_lst = age_lst.unique()

training_test = training_lst.value_counts()

#%%
"""
### titre du projet 
"""
title_lst = data_proj['6']

uniquetitle_lst = title_lst.unique()

title_test  = title_lst.value_counts()

#%%
text = title_lst.tolist()

collapsed_text = (' ').join(text)
collapsed_text2 = collapsed_text.replace(' de ', ' ').replace(' le ', ' ').replace(' pour ', ' ').replace(' du ', ' ').replace(' la ', ' ').replace(' à ', ' ').replace(' un ', ' ').replace(' une ', ' ').replace(' et ', ' ').replace(' des ', ' ')
collapsed_text3 = collapsed_text2.replace(' of ', ' ').replace(' the ', ' ').replace(' for ', ' ').replace(' in ', ' ').replace(' at ', ' ')

#%%
#wordcloud = WordCloud().generate(text[0])
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(collapsed_text3)

#%%
fname_plt = 'wordcloud_projecttitle.png'
fpath_plt = fdir_sav / fname_plt

plt.figure(0)
plt.clf()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout()
plt.savefig(fpath_plt)
plt.show()