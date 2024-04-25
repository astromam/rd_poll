#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 10:47:52 2024

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

fname_proj = 'results-survey149427_projets_2024-03-25_cleaned.xlsx'
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

ncol = 270 # data_labo_raw.head() and data_labo_raw.shape[1]
col_name = [str(x) for x in range(ncol)]

data_labo_raw = pd.read_excel(fpath_labo, header=0, names=col_name) # dimensions 181x415


#%%
"""
### Select the rows corresponding to the files of the people who went to the final page 
"""
#s2 = data_proj_raw['Dernière page']
# s2 = data_proj_raw['2']
# idx_finalpage = s2 == 8.0

# data_proj = data_proj_raw.loc[idx_finalpage,:]
data_labo = data_labo_raw.loc[:,:]

#%%
"""
### Liste de laboratoires
"""
labos_lst = data_labo['5']

uniquelabos_lst = labos_lst.unique()

labos_stats  = labos_lst.value_counts()

print(labos_stats)


#%%
"""
### Liste de soutien ou d'accords
"""
support_lst = data_labo['52']

uniquesupport_lst = support_lst.unique()

support_stats  = support_lst.value_counts()

print(support_stats)

#%%
"""
### Process the science keywords data
"""
### convert title_lst into a list
text52 = support_lst.tolist()
### join the words from all the input
collapsed_text52 = (' ').join(str(e) for e in text52)
### remove useless words in French
collapsed_text52_bis0 = collapsed_text52.replace(' le ', ' ').replace(' la ', ' ').replace(' les ', ' ').replace(' par ', ' ').replace(' pour ', ' ').replace(' sur ', ' ').replace(' d\'un ', ' ').replace(' d\'une ', ' ').replace(' d ', ' ').replace(' de ', ' ').replace(' du ', ' ').replace(' à ', ' ').replace(' aux ', ' ').replace(' ou ', ' ').replace(' un ', ' ').replace(' une ', ' ').replace(' et ', ' ').replace(' des ', ' ').replace(' en ', ' ').replace(' dans ', ' ')
collapsed_text52_bis = collapsed_text52_bis0.replace(' au ', ' ').replace(' avec ', ' ').replace('D ', ' ').replace(' est ', ' ').replace(' sont ', ' ').replace(' Le ', ' ')
### remove useless words in English
collapsed_text52_ter = collapsed_text52_bis.replace(' of ', ' ').replace(' the ', ' ').replace(' for ', ' ').replace(' in ', ' ').replace(' at ', ' ').replace(' nan ', ' ').replace('nan ', ' ')

#%%
"""
### Use WordCloud class to generate the data to plot
"""
support_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(collapsed_text52_ter)

#%%
"""
### plot of wordcloud for project titles
"""
fname_plt = 'wordcloud_labo_support_and_agreement.png'
fpath_plt = fdir_sav / fname_plt

plt.figure(0)
plt.clf()
plt.imshow(support_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Word cloud for support and agreements')
plt.tight_layout()
plt.savefig(fpath_plt)
plt.show()


#%%
"""
### Liste de besoins
"""
needs_lst = data_labo['89']

uniqueneeds_lst = needs_lst.unique()

needs_stats  = needs_lst.value_counts()

print(needs_stats)

#%%
"""
### Process the science keywords data
"""
### convert title_lst into a list
text89 = needs_lst.tolist()
### join the words from all the input
collapsed_text89 = (' ').join(str(e) for e in text52)
### remove useless words in French
collapsed_text89_bis0 = collapsed_text89.replace(' le ', ' ').replace(' la ', ' ').replace(' les ', ' ').replace(' par ', ' ').replace(' pour ', ' ').replace(' sur ', ' ').replace(' d\'un ', ' ').replace(' d\'une ', ' ').replace(' d ', ' ').replace(' de ', ' ').replace(' du ', ' ').replace(' à ', ' ').replace(' aux ', ' ').replace(' ou ', ' ').replace(' un ', ' ').replace(' une ', ' ').replace(' et ', ' ').replace(' des ', ' ').replace(' en ', ' ').replace(' dans ', ' ')
collapsed_text89_bis = collapsed_text89_bis0.replace(' au ', ' ').replace(' avec ', ' ').replace('D ', ' ').replace(' est ', ' ').replace(' sont ', ' ').replace(' Le ', ' ')
### remove useless words in English
collapsed_text89_ter = collapsed_text89_bis.replace(' of ', ' ').replace(' the ', ' ').replace(' for ', ' ').replace(' in ', ' ').replace(' at ', ' ').replace(' nan ', ' ').replace('nan ', ' ')

#%%
"""
### Use WordCloud class to generate the data to plot
"""
needs_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(collapsed_text89_ter)

#%%
"""
### plot of wordcloud for project titles
"""
fname_plt = 'wordcloud_labo_needs.png'
fpath_plt = fdir_sav / fname_plt

plt.figure(1)
plt.clf()
plt.imshow(support_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Word cloud for support and agreements')
plt.tight_layout()
plt.savefig(fpath_plt)
plt.show()


#%%
"""
### Liste de soutien ou d'accords
"""
support_lst_tmp = data_labo[['5','52']]

uniquesupport_lst_tmp = data_labo['52'].unique()

support_stats_tmp  = support_lst_tmp.value_counts()

print(support_stats_tmp)


#%%
"""
### Liste de besoins 4.1b
"""
needs_lst_tmp = data_labo[['5','89']]

uniqueneeds_lst_tmp = data_labo['89'].unique()

needs_stats_tmp  = needs_lst_tmp.value_counts()

print(needs_stats_tmp)

#%%
"""
### Liste de besoins 4.2b
"""
needs2_lst_tmp = data_labo[['5','94']]

uniqueneeds2_lst_tmp = data_labo['94'].unique()

needs2_stats_tmp  = needs2_lst_tmp.value_counts()

print(needs2_stats_tmp)

#%%
"""
### Liste de besoins 5.3b
"""
needs3_lst_tmp = data_labo[['5','170']]

uniqueneeds3_lst_tmp = data_labo['170'].unique()

needs3_stats_tmp  = needs3_lst_tmp.value_counts()

print(needs3_stats_tmp)

#%%
"""
### Liste de commentaires 6.9
"""
comments_lst_tmp = data_labo[['5','269']]

uniquecomments_lst_tmp = data_labo['269'].unique()

comments_stats_tmp  = comments_lst_tmp.value_counts()

print(comments_stats_tmp)

#%%
"""
### Liste de commentaires 5.1a
"""
envs_lst_tmp = data_labo[['5','151']]

uniqueenvs_lst_tmp = data_labo['151'].unique()

envs_stats_tmp  = envs_lst_tmp.value_counts()

print(envs_stats_tmp)

#%%
"""
### Liste de commentaires 5.1b
"""
envs2_lst_tmp = data_labo[['5','153']]

uniqueenvs2_lst_tmp = data_labo['153'].unique()

envs2_stats_tmp  = envs2_lst_tmp.value_counts()

print(envs2_stats_tmp)

#%%
"""
### Liste de commentaires 5.1c
"""
envs3_lst_tmp = data_labo[['5','155']]

uniqueenvs3_lst_tmp = data_labo['155'].unique()

envs3_stats_tmp  = envs3_lst_tmp.value_counts()

print(envs3_stats_tmp)

#%%
"""
### Liste de commentaires 5.1d
"""
envs4_lst_tmp = data_labo[['5','157']]

uniqueenvs4_lst_tmp = data_labo['157'].unique()

envs4_stats_tmp  = envs4_lst_tmp.value_counts()

print(envs4_stats_tmp)

#%%
"""
### Liste de commentaires 5.2a
"""
envs5_lst_tmp = data_labo[['5','159']]

uniqueenvs5_lst_tmp = data_labo['159'].unique()

envs5_stats_tmp  = envs5_lst_tmp.value_counts()

print(envs5_stats_tmp)

#%%
"""
### Liste de commentaires 5.2b
"""
envs6_lst_tmp = data_labo[['5','161']]

uniqueenvs6_lst_tmp = data_labo['161'].unique()

envs6_stats_tmp  = envs6_lst_tmp.value_counts()

print(envs6_stats_tmp)

#%%
"""
### Liste de commentaires 5.2c
"""
envs7_lst_tmp = data_labo[['5','163']]

uniqueenvs7_lst_tmp = data_labo['163'].unique()

envs7_stats_tmp  = envs7_lst_tmp.value_counts()

print(envs7_stats_tmp)

#%%
"""
### Liste de commentaires 5.2d
"""
envs8_lst_tmp = data_labo[['5','165']]

uniqueenvs8_lst_tmp = data_labo['165'].unique()

envs8_stats_tmp  = envs8_lst_tmp.value_counts()

print(envs8_stats_tmp)