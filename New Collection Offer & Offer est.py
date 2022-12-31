# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 23:07:25 2022

@author: Thomas
"""
import requests
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from importlib import reload
import numpy as np

data = pd.read_excel(r"E:\Thomas\Documents\Investing\Opensea Scraper\Activity Data\Nft_Activity_Data 1.xlsx", header= 0, decimal='.')

"Nan filter"
filter = [i for i, e in enumerate(data['Best_Offer']) if pd.isnull(e) == True or e == '---']
data = data.drop(filter)
data.reset_index(drop=True, inplace=True)

"points filter"
filter_points = [i for i, e in enumerate(data['Points']) if e < 2]
data = data.drop(filter_points)
data.reset_index(drop=True, inplace=True)

color = []
for k in data['Points']:
    if k == 0:
        color.append('black')
    if k == 1:
        color.append('red')
    if k == 2:
        color.append('orange')
    if k == 3:
        color.append('green')

sns.set_theme(style= 'darkgrid')

name = data['name'].tolist()
name_len = np.arange(len(name))

best_offer_eth = []
for g, h in enumerate(data['Best_Offer']):
    if h > 100:
        best_offer_eth.append(float(h) / 1228)
    else:
        best_offer_eth.append(h)

data['Best_Offer'] = best_offer_eth
best_offer = data['Best_Offer'].tolist()
best_offer_est = data['Best_Offer_Est'].tolist()
offer_difference = ((data['Best_Offer_Est'] - data['Best_Offer']) / data['Best_Offer_Est'] * 100).tolist()
#best_offer[17] = 0.1

f = plt.figure()
f.set_figwidth(20)
f.set_figheight(10)
plt.bar(name_len - 0.2, best_offer, 0.4, label = 'Best Offer', color = color)
plt.bar(name_len + 0.2, best_offer_est, 0.4, label = 'Best Offer Est', color = color, edgecolor = 'gray', linewidth = 2)
plt.xticks(name_len, name, rotation = 45, ha = 'right', label = offer_difference)
plt.legend()

fig, axs = plt.subplots(3, figsize=(20, 15))
plt.subplots_adjust(hspace = 1)

for c, d in enumerate(data['name']):
    axs[0].bar(d, data['Day_Sales'][c], color = color[c])
    axs[0].set(ylabel = 'Sales / Day')
    axs[0].set_xticklabels(data['name'], rotation=45, ha='right')

    axs[1].bar(d, data['Week_Sales'][c], color = color[c])
    axs[1].set(ylabel = 'Sales / Week Avg')
    axs[1].set_xticklabels(data['name'], rotation=45, ha='right')

    axs[2].bar(d, data['Month_Sales'][c], color = color[c])
    axs[2].set(ylabel = 'Sales / Month Avg')
    axs[2].set_xticklabels(data['name'], rotation=45, ha='right')


