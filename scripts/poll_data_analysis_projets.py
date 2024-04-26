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
### 1.1 Laboratoire de la personne porteuse du projet
"""
q101_lst = data_proj['5']

unique_q101_lst = q101_lst.unique()

q101_stats  = q101_lst.value_counts()

print(q101_stats)

#%%
"""
### 1.3 Statut de la personne porteuse du projet
"""
q103_lst = data_proj['7']

unique_q103_lst = q103_lst.unique()

q103_stats  = q103_lst.value_counts()

print(q103_stats)

#%%
"""
### 1.4 Genre de la personne porteuse du projet
"""
q104_lst = data_proj['9']

unique_q104_lst = q104_lst.unique()

q104_stats = q104_lst.value_counts()

print(q104_stats)

#%%
"""
### 1.5 Age de la personne porteuse du projet
"""
q105_lst = data_proj['10']

unique_q105_lst = q105_lst.unique()

q105_stats = q105_lst.value_counts()

print(q105_stats)

#%%
"""
### 1.6 Connaissance formation pour la personne ayant répondu
"""
q106_lst = data_proj['11']

unique_q106_lst = q106_lst.unique()

q106_stats = q106_lst.value_counts()

print(q106_stats)

#%%
"""
### 1.2 titre du projet 
"""
q102_lst = data_proj['6']

unique_q102_lst = q102_lst.unique()

q102_stats  = q102_lst.value_counts()

print(q102_stats)

#%%
"""
### Process the text data
"""
### convert title_lst into a list
text102 = q102_lst.tolist()
### join the words from all the input
collapsed_text102 = (' ').join(text102)
### remove useless words in French
collapsed_text102_bis = collapsed_text102.replace(' de ', ' ').replace(' le ', ' ').replace(' pour ', ' ').replace(' du ', ' ').replace(' la ', ' ').replace(' à ', ' ').replace(' un ', ' ').replace(' une ', ' ').replace(' et ', ' ').replace(' des ', ' ').replace(' en ', ' ').replace(' dans ', ' ')
### remove useless words in English
collapsed_text102_ter = collapsed_text102_bis.replace(' of ', ' ').replace(' the ', ' ').replace(' for ', ' ').replace(' in ', ' ').replace(' at ', ' ')

#%%
"""
### Use WordCloud class to generate the data to plot
"""
q102_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(collapsed_text102_ter)

#%%
"""
### plot of wordcloud for project titles
"""
fname_plt = 'wordcloud_q102_projecttitle.png'
fpath_plt = fdir_sav / fname_plt

plt.figure(0)
plt.clf()
plt.imshow(q102_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Word cloud for project titles')
plt.tight_layout()
plt.savefig(fpath_plt)
plt.show()

#%%
"""
### 2.2 Question scientifique qui motive le projet
"""
q202_lst = data_proj['27']

unique_q202_lst = q202_lst.unique()

q202_stats  = q202_lst.value_counts()

print(q202_stats)

#%%
"""
### Process the science question data
"""
### convert title_lst into a list
text202 = q202_lst.tolist()
### join the words from all the input
collapsed_text202 = (' ').join(str(e) for e in text202)
### remove useless words in French
collapsed_text202_bis = collapsed_text202.replace(' le ', ' ').replace(' la ', ' ').replace(' les ', ' ').replace(' par ', ' ').replace(' pour ', ' ').replace(' sur ', ' ').replace(' d\'un ', ' ').replace(' d\'une ', ' ').replace(' d ', ' ').replace(' de ', ' ').replace(' du ', ' ').replace(' à ', ' ').replace(' aux ', ' ').replace(' ou ', ' ').replace(' un ', ' ').replace(' une ', ' ').replace(' et ', ' ').replace(' des ', ' ').replace(' en ', ' ').replace(' dans ', ' ')
### remove useless words in English
collapsed_text202_ter = collapsed_text202_bis.replace(' of ', ' ').replace(' the ', ' ').replace(' for ', ' ').replace(' in ', ' ').replace(' at ', ' ').replace(' nan ', ' ').replace('nan ', ' ')

#%%
"""
### Use WordCloud class to generate the data to plot
"""
q202_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(collapsed_text202_ter)

#%%
"""
### plot of wordcloud for project titles
"""
fname_plt = 'wordcloud_q202_sci_question.png'
fpath_plt = fdir_sav / fname_plt

plt.figure(1)
plt.clf()
plt.imshow(q202_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Word cloud for science questions')
plt.tight_layout()
plt.savefig(fpath_plt)
plt.show()

#%%
"""
### 2.4 Mots-clé
"""
q204_lst = data_proj['32']

unique_q204_lst = q204_lst.unique()

q204_stats  = q204_lst.value_counts()

print(q204_stats)

#%%
"""
### Process the science keywords data
"""
### convert title_lst into a list
text204 = q204_lst.tolist()
### join the words from all the input
collapsed_text204 = (' ').join(str(e) for e in text204)
### remove useless words in French
collapsed_text204_bis = collapsed_text204.replace(' le ', ' ').replace(' la ', ' ').replace(' les ', ' ').replace(' par ', ' ').replace(' pour ', ' ').replace(' sur ', ' ').replace(' d\'un ', ' ').replace(' d\'une ', ' ').replace(' d ', ' ').replace(' de ', ' ').replace(' du ', ' ').replace(' à ', ' ').replace(' aux ', ' ').replace(' ou ', ' ').replace(' un ', ' ').replace(' une ', ' ').replace(' et ', ' ').replace(' des ', ' ').replace(' en ', ' ').replace(' dans ', ' ')
### remove useless words in English
collapsed_text204_ter = collapsed_text204_bis.replace(' of ', ' ').replace(' the ', ' ').replace(' for ', ' ').replace(' in ', ' ').replace(' at ', ' ').replace(' nan ', ' ').replace('nan ', ' ')

#%%
"""
### Use WordCloud class to generate the data to plot
"""
q204_wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(collapsed_text204_ter)

#%%
"""
### plot of wordcloud for project titles
"""
fname_plt = 'wordcloud_q204_sci_keywords.png'
fpath_plt = fdir_sav / fname_plt

plt.figure(2)
plt.clf()
plt.imshow(q204_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Word cloud for science keywords')
plt.tight_layout()
plt.savefig(fpath_plt)
plt.show()

#%%
# """
# ### 3.2b Durée projet
# """
# project_duration_lst = data_proj['46']

# uniqueproject_duration_lst = project_duration_lst.unique()

# project_duration_stats = project_duration_lst.value_counts()

# print(project_duration_stats)

#%%
"""
### Q4.5 - Nature des partenariats industriels (colonnes GE à GK) - 7*26+5-1 (186)  à 7*26+11-1 (192)
"""
q405_nIni = 186
q405_nEnd = 192
q405_nPts = q405_nEnd-q405_nIni+1

q405_idx_arr = q405_nIni+ np.arange(q405_nPts)


for i in q405_idx_arr:
    
    print(f'column name: {i}')
    q405_lst = data_proj[f'{i}']
    
    q405_partnership_lst = q405_lst.unique()
    
    q405_stats  = q405_lst.value_counts()
    
    print(q405_stats)
    print('\n')


#%%
"""
### Q4.6 - Si applicable, détail des partenariats industriels (colonnes GL à GP) - 7*26+12-1 (193)  à 7*26+16-1 (197)
"""
q406_nIni = 193
q406_nEnd = 197
q406_nPts = q406_nEnd-q406_nIni+1

q406_idx_arr = q406_nIni+ np.arange(q406_nPts)


for i in q406_idx_arr:
    
    print(f'column name: {i}')
    q406_lst = data_proj[f'{i}']
    
    unique_q406_lst = q406_lst.unique()
    
    q406_stats  = q406_lst.value_counts()
    
    print(q406_stats)
    print('\n')

#%%
"""
### Q5.1 - Ressources humaines totales consacrées au projet de R&D  (colonnes GQ à HF) - 7*26+17-1 (198) à 8*26+6-1 (213)
"""
val = 199

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
val = 265

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
    
#%%
"""
### Q5.4 - Détails des moyens techniques utilisées pour le projet de R&D (colonnes JH à JT) - 10*26+8-1 (267) à 10*26+20-1 (279)
"""
val = 267

q504_nIni = 267
q504_nEnd = 279
q504_nPts = q504_nEnd-q504_nIni+1

q504_idx_arr = q504_nIni + np.arange(q504_nPts)

for i in q504_idx_arr:
    
    print(f'column name: {i}')
    q504_lst = data_proj[f'{i}']
    
    unique_q504_lst = q504_lst.unique()
    
    q504_stats  = q504_lst.value_counts()
    
    print(q504_stats)
    print('\n')

#%%
"""
### Q5.5 - D’après vous, quels sont les outils à privilégier pour les futurs besoins en R&D ? (colonnes JU à KG) - 10*26+21-1 (280) à 11*26+7-1 (292)
"""
val = 267

q505_nIni = 280
q505_nEnd = 292
q505_nPts = q505_nEnd-q505_nIni+1

q505_idx_arr = q505_nIni + np.arange(q505_nPts)

for i in q505_idx_arr:
    
    print(f'column name: {i}')
    q505_lst = data_proj[f'{i}']
    
    unique_q505_lst = q505_lst.unique()
    
    q505_stats  = q505_lst.value_counts()
    
    print(q505_stats)
    print('\n')
    
#%%
"""
### Q7.1 - Quel est le niveau de contrainte environnementale imposé par le cadre institutionnel (e.g. CNRS, universités, CNES) et/ou par des organismes partenaires ? (colonnes NJ à NQ) - 14*26+10-1 (373) à 14*26+17-1 (380)
"""
val = 373

q701_nIni = 373
q701_nEnd = 380
q701_nPts = q701_nEnd-q701_nIni+1

q701_idx_arr = q701_nIni + np.arange(q701_nPts)

for i in q701_idx_arr:
    
    print(f'column name: {i}')
    q701_lst = data_proj[f'{i}']
    
    unique_q701_lst = q701_lst.unique()
    
    q701_stats  = q701_lst.value_counts()
    
    print(q701_stats)
    print('\n')
    
#%%
"""
### Q7.2 - Quel est le niveau de contrainte environnementale imposé par le cadre institutionnel (e.g. CNRS, universités, CNES) et/ou par des organismes partenaires ? (colonnes NR à NY) - 14*26+18-1 (381) à 14*26+25-1 (388)
"""
val = 267

q702_nIni = 381
q702_nEnd = 388
q702_nPts = q702_nEnd-q702_nIni+1

q702_idx_arr = q702_nIni + np.arange(q702_nPts)

for i in q702_idx_arr:
    
    print(f'column name: {i}')
    q702_lst = data_proj[f'{i}']
    
    unique_q702_lst = q702_lst.unique()
    
    q702_stats  = q702_lst.value_counts()
    
    print(q702_stats)
    print('\n')
 
#%%
"""
### Q7.3a - Avez-vous déjà intégré la question environnementale dans vos travaux/propositions de R&D ? (colonnes NZ à OD) - 14*26+16-1 (389) à 15*26+4-1 (393)
"""
val = 267

q703_nIni = 389
q703_nEnd = 393
q703_nPts = q703_nEnd-q703_nIni+1

q703_idx_arr = q703_nIni + np.arange(q703_nPts)

for i in q703_idx_arr:
    
    print(f'column name: {i}')
    q703_lst = data_proj[f'{i}']
    
    unique_q703_lst = q703_lst.unique()
    
    q703_stats  = q703_lst.value_counts()
    
    print(q703_stats)
    print('\n')

    
#%%
"""
### Q7.4 - Soutiendrez-vous des projets R&D matérielle et numérique visant à réduire l’impact environnemental des activités de R&D ? (colonnes OE à OL) - 15*26+5-1 (394) à 15*26+12-1 (401)
"""
val = 267

q704_nIni = 394
q704_nEnd = 401
q704_nPts = q704_nEnd-q704_nIni+1

q704_idx_arr = q704_nIni + np.arange(q704_nPts)

for i in q704_idx_arr:
    
    print(f'column name: {i}')
    q704_lst = data_proj[f'{i}']
    
    unique_q704_lst = q704_lst.unique()
    
    q704_stats  = q704_lst.value_counts()
    
    print(q704_stats)
    print('\n')

    