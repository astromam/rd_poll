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
### Liste de laboratoires
"""
labos_lst = data_proj['5']

uniquelabos_lst = labos_lst.unique()

labos_stats  = labos_lst.value_counts()

print(labos_stats)

#%%
"""
### Personnel ayant répondu
"""
personnel_lst = data_proj['7']

uniquepersonnel_lst = personnel_lst.unique()

personnel_stats  = personnel_lst.value_counts()

print(personnel_stats)

#%%
"""
### Genre de la personne ayant répondu
"""
gender_lst = data_proj['9']

uniquegender_lst = gender_lst.unique()

gender_stats = gender_lst.value_counts()

print(gender_stats)

#%%
"""
### Age de la personne ayant répondu
"""
age_lst = data_proj['10']

uniqueage_lst = age_lst.unique()

age_stats = age_lst.value_counts()

print(age_stats)

#%%
"""
### Connaissance formation pour la personne ayant répondu
"""
training_lst = data_proj['11']

uniquetraining_lst = training_lst.unique()

training_stats = training_lst.value_counts()

print(training_stats)

#%%
"""
### titre du projet 
"""
title_lst = data_proj['6']

uniquetitle_lst = title_lst.unique()

title_stats  = title_lst.value_counts()

print(title_stats)

#%%
"""
### Process the text data
"""
### convert title_lst into a list
text = title_lst.tolist()
### join the words from all the input
collapsed_text = (' ').join(text)
### remove useless words in French
collapsed_text_bis = collapsed_text.replace(' de ', ' ').replace(' le ', ' ').replace(' pour ', ' ').replace(' du ', ' ').replace(' la ', ' ').replace(' à ', ' ').replace(' un ', ' ').replace(' une ', ' ').replace(' et ', ' ').replace(' des ', ' ').replace(' en ', ' ').replace(' dans ', ' ')
### remove useless words in English
collapsed_text_ter = collapsed_text_bis.replace(' of ', ' ').replace(' the ', ' ').replace(' for ', ' ').replace(' in ', ' ').replace(' at ', ' ')

#%%
"""
### Use WordCloud class to generate the data to plot
"""
title_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(collapsed_text_ter)

#%%
"""
### plot of wordcloud for project titles
"""
fname_plt = 'wordcloud_projecttitle.png'
fpath_plt = fdir_sav / fname_plt

plt.figure(0)
plt.clf()
plt.imshow(title_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Word cloud for project titles')
plt.tight_layout()
plt.savefig(fpath_plt)
plt.show()

#%%
"""
### Question scientifique qui motive le projet
"""
sci_question_lst = data_proj['27']

uniquesci_question_lst = sci_question_lst.unique()

sci_question_stats  = sci_question_lst.value_counts()

print(sci_question_stats)

#%%
"""
### Process the science question data
"""
### convert title_lst into a list
text27 = sci_question_lst.tolist()
### join the words from all the input
collapsed_text27 = (' ').join(str(e) for e in text27)
### remove useless words in French
collapsed_text27_bis = collapsed_text27.replace(' le ', ' ').replace(' la ', ' ').replace(' les ', ' ').replace(' par ', ' ').replace(' pour ', ' ').replace(' sur ', ' ').replace(' d\'un ', ' ').replace(' d\'une ', ' ').replace(' d ', ' ').replace(' de ', ' ').replace(' du ', ' ').replace(' à ', ' ').replace(' aux ', ' ').replace(' ou ', ' ').replace(' un ', ' ').replace(' une ', ' ').replace(' et ', ' ').replace(' des ', ' ').replace(' en ', ' ').replace(' dans ', ' ')
### remove useless words in English
collapsed_text27_ter = collapsed_text27_bis.replace(' of ', ' ').replace(' the ', ' ').replace(' for ', ' ').replace(' in ', ' ').replace(' at ', ' ').replace(' nan ', ' ').replace('nan ', ' ')

#%%
"""
### Use WordCloud class to generate the data to plot
"""
sci_question_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(collapsed_text27_ter)

#%%
"""
### plot of wordcloud for project titles
"""
fname_plt = 'wordcloud_sci_question.png'
fpath_plt = fdir_sav / fname_plt

plt.figure(1)
plt.clf()
plt.imshow(sci_question_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Word cloud for science questions')
plt.tight_layout()
plt.savefig(fpath_plt)
plt.show()

#%%
"""
### Mots-clé
"""
sci_keywords_lst = data_proj['32']

uniquesci_keywords_lst = sci_keywords_lst.unique()

sci_keywords_stats  = sci_keywords_lst.value_counts()

print(sci_keywords_stats)

#%%
"""
### Process the science keywords data
"""
### convert title_lst into a list
text32 = sci_keywords_lst.tolist()
### join the words from all the input
collapsed_text32 = (' ').join(str(e) for e in text32)
### remove useless words in French
collapsed_text32_bis = collapsed_text32.replace(' le ', ' ').replace(' la ', ' ').replace(' les ', ' ').replace(' par ', ' ').replace(' pour ', ' ').replace(' sur ', ' ').replace(' d\'un ', ' ').replace(' d\'une ', ' ').replace(' d ', ' ').replace(' de ', ' ').replace(' du ', ' ').replace(' à ', ' ').replace(' aux ', ' ').replace(' ou ', ' ').replace(' un ', ' ').replace(' une ', ' ').replace(' et ', ' ').replace(' des ', ' ').replace(' en ', ' ').replace(' dans ', ' ')
### remove useless words in English
collapsed_text32_ter = collapsed_text32_bis.replace(' of ', ' ').replace(' the ', ' ').replace(' for ', ' ').replace(' in ', ' ').replace(' at ', ' ').replace(' nan ', ' ').replace('nan ', ' ')

#%%
"""
### Use WordCloud class to generate the data to plot
"""
sci_keywords_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(collapsed_text32_ter)

#%%
"""
### plot of wordcloud for project titles
"""
fname_plt = 'wordcloud_sci_keywords.png'
fpath_plt = fdir_sav / fname_plt

plt.figure(2)
plt.clf()
plt.imshow(sci_keywords_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Word cloud for science keywords')
plt.tight_layout()
plt.savefig(fpath_plt)
plt.show()

#%%
"""
### Durée projet
"""
project_duration_lst = data_proj['46']

uniqueproject_duration_lst = project_duration_lst.unique()

project_duration_stats = project_duration_lst.value_counts()

print(project_duration_stats)
