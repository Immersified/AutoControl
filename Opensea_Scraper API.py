# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 20:40:22 2022

@author: Thomas
"""
import requests
import pandas as pd
import re

data = pd.read_excel(r"E:\Thomas\Documents\Investing\Nft info\Nft Bidding\Nft_Bidding_Rankings.xlsx", header= 0, sep='\t', decimal='.')
link = data['Link']

url_test = link[2].replace("https://opensea.io/collection/", "https://api.opensea.io/api/v1/collection/") + "/stats"
url = url_test
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers).text

Change_1D = []
Avg_price_1D = []
Difference_1D = []

test = re.findall('[:].....', response)

if "seven_day_volume" in response:
    print("Yes")
else:
    print("No")
