# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:36:04 2019

@author: udayjuttu
source: 'https://www.numbeo.com/cost-of-living/country_result.jsp?country=United+States'
"""
import numpy as np
import random
random.seed(0)
import bs4 as bs
import urllib.request
import pandas as pd
from wiki import dataframe
from wiki import field_scraping

#intiating dataframe
df=dataframe()

# Considering only 
cost_index_columns=field_scraping('https://www.numbeo.com/cost-of-living/country_result.jsp?country=United+States','table','id','t2','th')
cost_index_data=field_scraping('https://www.numbeo.com/cost-of-living/country_result.jsp?country=United+States','table','id','t2','td')

# Data Cleaning to store it in dataframe
rank_living_cost_index=[]
city_2=[]
new_city_2=[]
cost_index_rate=[]
rent_index=[]
cost_plus_rent_index=[]
groceries_index=[]
restaurant_price_index=[]
power_index=[]

j=1
case_list=[]
for i in range(0,49,1):
    rank={cost_index_data[j]:(i+1)}
    cost={cost_index_data[j]:cost_index_data[j+1]}
    rent={cost_index_data[j]:cost_index_data[j+2]}
    cost_plus_rent={cost_index_data[j]:cost_index_data[j+3]}
    groceries={cost_index_data[j]:cost_index_data[j+4]}
    restaurant={cost_index_data[j]:cost_index_data[j+5]}
    power={cost_index_data[j]:cost_index_data[j+6]}
    rank_living_cost_index.append(rank)
    city_2.append(cost_index_data[j])
    cost_index_rate.append(cost)
    rent_index.append(rent)
    cost_plus_rent_index.append(cost_plus_rent)
    groceries_index.append(groceries)
    restaurant_price_index.append(restaurant)
    power_index.append(power)
    j=j+8

for city in city_2:
    city=city.split(',')
    city=city[0]
    new_city_2.append(city)
    
def aggregated_dataframe():
#initiating some list to
    sorted_cities=[]
    index_val=[]
    rank=[]
    cost=[]
    rent=[]
    cost_rent=[]
    groceries=[]
    restaurant=[]
    power=[]
#using Enumerate to save the index of new_city_2 that matches to city_names
    for i,k in enumerate(new_city_2):
        for city_names in df['City']:
                if str(k)==str(city_names):
                      sorted_cities.append(i)
                      index_val.append(df.index[df['City']==city_names].tolist())    
# we have all index's of our previous dataframe that matches to new columns(new_city_2)                      
    for i in sorted_cities:
       rank.append(np.array(list(rank_living_cost_index[i].values()),dtype=int))
       cost.append(np.array(list(cost_index_rate[i].values()),dtype=float))
       rent.append(np.array(list(rent_index[i].values()),dtype=float))  
       cost_rent.append(np.array(list(cost_plus_rent_index[i].values()),dtype=float))
       groceries.append(np.array(list(groceries_index[i].values()),dtype=float))
       restaurant.append(np.array(list(restaurant_price_index[i].values()),dtype=float))
       power.append(np.array(list(power_index[i].values()),dtype=float))
    
#adding the this coloum to the original dataframe
    for i in range(len(index_val)):
        df.loc[index_val[i][0],'rank_living_cost_index']=rank[i][0]
        df.loc[index_val[i][0],'cost_index_rate']=cost[i][0]
        df.loc[index_val[i][0],'rate_index']=rent[i][0]
        df.loc[index_val[i][0],'cost_plus_rent_index']=cost_rent[i][0]
        df.loc[index_val[i][0],'groceries_index']=groceries[i][0]
        df.loc[index_val[i][0],'restaurent_price_index']=restaurant[i][0]
        df.loc[index_val[i][0],'power_index']=power[i][0]
    return df