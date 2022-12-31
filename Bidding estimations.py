# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:48:41 2022

@author: Thomas
"""
import requests
import pandas as pd
import re


data = pd.read_excel(r"C:\Users\Administrator\Documents\AutoBidder\Bid_Links_In.xlsx", header= 0, decimal='.')

link = data['Link']
royalty_set = data['Royalty'] + 2.5

floor_price = []
bid_price = []
royalty = []
royalty_change = []

test = royalty_set[0]

for a, b in enumerate(link):
    url_test = b.replace("https://opensea.io/collection/", "https://api.opensea.io/api/v1/collection/")
    headers = {"Accept": "application/json"}

    response = requests.get(url_test, headers=headers).text
    response_stats = re.findall('stats.*' , response)

    if response != '{"success":false}':
        "Name filter"
        name =  b.replace("https://opensea.io/collection/", "")
    
        "Stats filter"
        filter_stats = re.findall(':(.+?),' , response_stats[0])
        floor_price_fix = re.findall('"floor_price":(.+?)}', response_stats[0])

        filter_roy = re.findall('"seller_fee_basis_points":.*' , response)
        if not filter_roy:
            filter_roy.append(str(0.0))
        filter_royalty = re.findall(':(.+?),' , filter_roy[0])

        floor_price.append(float(floor_price_fix[0]))
        royalty.append(float(filter_royalty[0]) / 100)
        royalty_change.append(royalty[a] - royalty_set[a])
        profit_percentage = 0.025 * float(floor_price_fix[0]) + 0.85
        if profit_percentage > 0.90:
            profit_percentage = 0.90
        bid_price.append(float(floor_price_fix[0]) * ((100 - (royalty[a] - royalty_change[a])) / 100) * profit_percentage)
        
data['Floor'] = floor_price
data['Bid price'] = bid_price

data.to_excel('Bid Links Out.xlsx')

