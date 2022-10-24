# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:13:38 2022

@author: Thomas
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from importlib import reload
import seaborn as sns

data_all = pd.read_excel(r"E:\Thomas\Documents\Investing\NFT's\Nft Bidding Rankings.xlsx", header= 0, decimal='.')

data_all = data_all.dropna()
data_all.reset_index(drop=True, inplace=True)

collections = []
for i in data_all['Name']:
    if i not in collections:
        collections.append(i)

dic = dict(iter(data_all.iloc[:len(data_all['Name'])]
    .groupby(data_all['Name'])))

for k, l in enumerate(collections):
    dic[l].reset_index(drop=True, inplace=True)
    if len(dic[l]) < 40 or len(dic[l]) > 70:
        dic.pop(collections[k])

collections_final = list(dic.keys())

length = []
for c in collections_final:
    length.append(len(dic[c]. index))

profit_avg = []
profit_floor_avg = []

for a, b in enumerate(collections_final):
    average = dic[collections_final[a]]
    average_final = np.average(average['Profit'])
    profit_avg.append(average_final)
    dic[collections_final[a]]['Profit Avg'] = average_final

    average_2 = dic[collections_final[a]]
    average_final_2 = np.average(average_2['Profit / Floor (%)'])
    profit_floor_avg.append(average_final_2)
    dic[collections_final[a]]['Profit / Floor (%) Avg'] = average_final_2

sns.set_theme(style= 'darkgrid')

fig, axs = plt.subplots(2, figsize=(20, 10))
plt.subplots_adjust(hspace = 1)

axs[0].bar(collections_final, profit_avg)
axs[0].set(ylabel = 'Profit in ($E$)')
axs[0].set_xticklabels(collections_final, rotation=45, ha='right')

axs[1].bar(collections_final, profit_floor_avg)
axs[1].set(ylabel = 'Profit / Floor in (%)')
axs[1].set_xticklabels(collections_final, rotation=45, ha='right')


