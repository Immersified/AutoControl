# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:32:58 2022

@author: Thomas
"""
import requests
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from importlib import reload

data = pd.read_excel(r"E:\Thomas\Documents\Investing\Opensea Scraper\Bid_Links_In.xlsx", header= 0, decimal='.')

#data = data2[:7]

link = data['Link']
names = []
day_sales = []
week_avg_sales = []
month_avg_sales = []
points = []
floor_price = []

"Settings:"
floor_low = 0.3
floor_high = 3
activity_low = 5
activity_high = 25


for a, b in enumerate(link):
    url_test = b.replace("https://opensea.io/collection/", "https://api.opensea.io/api/v1/collection/") + "/stats"
    headers = {"Accept": "application/json"}

    response = requests.get(url_test, headers=headers).text

    "Name filter"
    name =  b.replace("https://opensea.io/collection/", "")

    "Stats filter"
    filter_stats = re.findall(':(.+?),' , response)
    filter_stats[0] = filter_stats[0].replace("""{"one_hour_volume":""", "")
    floor_price_fix = re.findall('"floor_price":(.+?)}', response)
    filter_stats.append(floor_price_fix[0])

    "Append"
    day_sales.append(float(filter_stats[14]))
    week_avg_sales.append(float(filter_stats[20]) / 7)
    month_avg_sales.append(float(filter_stats[25]) / 365 * 12)

    names.append(name)

    "Floor price filter"
    if float(filter_stats[36]) >= floor_low and float(filter_stats[36]) <= floor_high:
        floor_price.append(1)
    else:
        floor_price.append(0)

    "Actvity filters"
    if float(filter_stats[14]) >= activity_low and float(filter_stats[14]) <= activity_high:
        points.append(1)
    else:
        points.append(0)

    if (float(filter_stats[20]) / 7) >= activity_low and (float(filter_stats[20]) / 7) <= activity_high:
        points[a] += 1
    else:
        points[a] += 0

    if (float(filter_stats[25]) / 365 * 12) >= activity_low and (float(filter_stats[25]) / 365 * 12) <= activity_high:
        points[a] += 1
    else:
        points[a] += 0

color = []
for k in points:
    if k == 0:
        color.append('black')
    if k == 1:
        color.append('red')
    if k == 2:
        color.append('orange')
    if k == 3:
        color.append('green')

sns.set_theme(style= 'darkgrid')

fig, axs = plt.subplots(3, figsize=(20, 15))
plt.subplots_adjust(hspace = 1)

for c, d in enumerate(day_sales):
    axs[0].bar(names[c], day_sales[c], color = color[c])
    axs[0].set(ylabel = 'Sales / Day')
    axs[0].set_xticklabels(names, rotation=45, ha='right')

    axs[1].bar(names[c], week_avg_sales[c], color = color[c])
    axs[1].set(ylabel = 'Sales / Week Avg')
    axs[1].set_xticklabels(names, rotation=45, ha='right')

    axs[2].bar(names[c], month_avg_sales[c], color = color[c])
    axs[2].set(ylabel = 'Sales / Month Avg')
    axs[2].set_xticklabels(names, rotation=45, ha='right')

for k, i in enumerate(floor_price):
    if i == 1:
        axs[0].get_xticklabels()[k].set_color('green')
        axs[1].get_xticklabels()[k].set_color('green')
        axs[2].get_xticklabels()[k].set_color('green')