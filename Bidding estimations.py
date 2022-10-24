# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:48:41 2022

@author: Thomas
"""
import requests
import pandas as pd
import re


data = pd.read_excel(r"E:\Thomas\Documents\Investing\Opensea Scraper\Bid Links In.xlsx", header= 0, decimal='.')

link = data['Link']
royalty = data['Royalty']

floor_price = []
bid_price = []

for a, b in enumerate(link):
    url_test = b.replace("https://opensea.io/collection/", "https://api.opensea.io/api/v1/collection/") + "/stats"
    headers = {"Accept": "application/json"}

    response = requests.get(url_test, headers=headers).text

    floor_price_fix = re.findall('"floor_price":(.+?)}', response)
    floor_price.append(float(floor_price_fix[0]))

    bid_price_fix = floor_price[a] * ((100-royalty[a] - 2.5)/100) * (0.02 / 1 * floor_price[a] + 0.85)
    bid_price.append(bid_price_fix)

data['Floor'] = floor_price
data['Bid price'] = bid_price

data.to_excel('Bid Links Out.xlsx')

