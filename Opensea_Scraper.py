# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 13:15:42 2022

@author: Thomas
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from importlib import reload
plt=reload(plt)

data = pd.read_excel(r"E:\Thomas\Downloads\Nft_Table 83.xlsx", header= 0, decimal='.')

best_offer = []

for a in data['Best offer']:
    if a == '< 0.01':
        meme = float(a.replace('<', ''))
        best_offer.append(meme)
    else:
        best_offer.append(a)

data['Best offer'] = best_offer

floor_price = []

for b in data['Floor']:
    if b == '< 0.01':
        meme = float(b.replace('<', ''))
        floor_price.append(meme)
    else:
        floor_price.append(b)

data['Floor'] = floor_price

Royalty = data['Royalty'] * 100
data['Royalty'] = Royalty

supply = data['Supply']
"Supply column filter"
filter = [i for i, e in enumerate(supply) if e == '---' or pd.isnull(e) == True or e < 100]
supply_filter = data.drop(filter)
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
filter3 = [i for i, e in enumerate(data_filter['Floor']) if e <= 0.3 or e >= 1.8 or e == '---']
data_filter_final = data_filter.drop(filter3)
data_filter_final.reset_index(drop=True, inplace=True)

Listings = data_filter_final['Act.Listings'] * data_filter_final['Supply']
data_filter_final['Act.Listings'] = Listings

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
