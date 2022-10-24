# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:17:32 2022

@author: Thomas
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from importlib import reload
import seaborn as sns
plt=reload(plt)

data = pd.read_excel(r"E:\Thomas\Downloads\Nft_Table 122.xlsx", header= 0, decimal='.')

data_all = pd.DataFrame()

for k in range(122):
    data = pd.read_excel(r"E:\Thomas\Documents\Investing\Opensea Scraper\Nftfiles\Nft_Table " + str(k) + ".xlsx", header= 0, decimal='.')
    data_all = pd.concat([data_all, data])

data_all = data_all.dropna()
data_all.reset_index(drop=True, inplace=True)

best_offer = []

filter_name = [i for i, e in enumerate(data_all['Name']) if e == 'ApeX NFT Predator' or e == 'UNDERWATER CLUB OfficaI']
data_all = data_all.drop(filter_name)
data_all.reset_index(drop=True, inplace=True)

for a in data_all['Best offer']:
    if a == '< 0.01':
        meme = float(a.replace('<', ''))
        best_offer.append(meme)
    else:
        best_offer.append(a)

data_all['Best offer'] = best_offer

floor_price = []

for b in data_all['Floor']:
    if b == '< 0.01':
        meme = float(b.replace('<', ''))
        floor_price.append(meme)
    else:
        floor_price.append(b)

data_all['Floor'] = floor_price

supply = data_all['Supply']
"Supply column filter"
filter = [i for i, e in enumerate(supply) if e == '---' or pd.isnull(e) == True or e < 100]
supply_filter = data_all.drop(filter)
supply_filter.reset_index(drop=True, inplace=True)

"Listing filter"
filter1 = [i for i, e in enumerate(supply_filter['Act.Listings']) if e == 0 or pd.isnull(e) == True]
supply_filter1 = supply_filter.drop(filter1)
supply_filter1.reset_index(drop=True, inplace=True)

"Best offer filter"
filter2 = [i for i, e in enumerate(supply_filter1['Best offer']) if e == '---']
data_filter = supply_filter1.drop(filter2)
data_filter_nobids = supply_filter1.filter(items = filter2, axis = 0)
data_filter.reset_index(drop=True, inplace=True)

"Floor price filter"
filter3 = [i for i, e in enumerate(data_filter['Floor']) if e <= 0.8 or e >= 1.5 or e == '---']
data_filter_final = data_filter.drop(filter3)
data_filter_final.reset_index(drop=True, inplace=True)

Royalty = []

for k in data_filter_final['Royalty']:
    if k < 1:
        Royalty.append(k*100)
    else:
        Royalty.append(k)

data_filter_final['Royalty'] = Royalty

"Quick Maths"
profit = data_filter_final['Floor']*(100-(data_filter_final['Royalty'] + 2.5))/100-data_filter_final['Best offer']
data_filter_final['Profit'] = profit

filter4 = [i for i, e in enumerate(data_filter_final['Profit']) if e <= 0]
data_filter_profit = data_filter_final.drop(filter4)
data_filter_profit.reset_index(drop=True, inplace=True)

profit_floor = data_filter_profit['Profit']/data_filter_profit['Floor'] * 100
data_filter_profit['Profit / Floor (%)'] = profit_floor
sales_list = data_filter_profit['Sales 1D'] / data_filter_profit['Act.Listings'] * 100
data_filter_profit['Sales / List (%)'] = sales_list

"Best item factor"
data_filter_profit['Ranking'] = data_filter_profit['Profit / Floor (%)'] * 2 + data_filter_profit['Sales / List (%)']

"Sorting based on Ranking"
data_filter_profit.sort_values(by=['Ranking'], ascending = False, inplace = True)
data_filter_profit.reset_index(drop=True, inplace=True)

"Export file"
data_filter_profit.to_excel('Nft Bidding Rankings.xlsx')

data_all = data_filter_profit

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