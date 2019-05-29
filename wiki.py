# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:17:48 2019
@author: udayjuttu
data taken from the source 'https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population'
"""
## Import necessary libraries 
import random
random.seed(0)
import bs4 as bs
import urllib.request
import pandas as pd
import re

## Field Scraping
def field_scraping(url,attribute,sub_attribute,field_name,field):
    info=urllib.request.urlopen(url).read()
    soup=bs.BeautifulSoup(info,'lxml')
    table=soup.find(attribute,{sub_attribute:field_name})
    title=table.find_all(field)
    tex=[]
    nex=[]
    for i in title:
        k= str(i.text)
        tex.append(k) 
    for i in range(len(tex)):
        val=re.split('\n',tex[i])
        nex.append(val[0])
    return nex
         
## Calling function to get the Column's Attributes            
columns=field_scraping('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population','table','class','wikitable sortable','th')

## Adding extra columns 
columns.insert(7,'2016 land area in km2')
columns.insert(9,'2016 population density in km2')
columns[2]='state'
columns[6]='2016 land area in sq/mi'
columns[8]='2016 population density in sq/mi'

Attributes=columns
## lets grab the data into this columns field

## Performing Data munging to push the entire data into pandas Dataframe
data=field_scraping('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population','table','class','wikitable sortable','td')

rank=[]
city=[]
state=[]
estimate_18=[]
census=[]
change=[]
area_insq=[]
area_inkm=[]
population_insq=[]
population_inkm=[]
location=[]
j=0

## Since we have 314 cities we took range from 0-314
for i in range(0,314,1):
    rank.append(int(data[j].strip("'")))
    city.append(data[j+1].strip('[d]').replace(',',''))
    state.append(data[j+2].strip('\xa0').replace(',',''))
    estimate_18.append(data[j+3].strip(',').replace(',',''))
    census.append(data[j+4].strip(',').replace(',',''))
    change.append((data[j+5].strip('%')).replace(',',''))
    area_insq.append(data[j+6].strip('\xa0sq\xa0mi').replace(',',''))
    area_inkm.append(data[j+7].strip('\xa0km2').replace(',',''))
    population_insq.append(data[j+8].strip('/sq\xa0mi').replace(',',''))
    population_inkm.append(data[j+9].replace('/km2','').replace(',',''))
    location.append(data[j+10].strip('\ufeff / \ufeff40').replace(',',''))
    j=j+11

city_name=[]
for i in city:
    i=i.split('[')
    city_name.append(i[0])

## Moving data to pandas Dataframe with Attributes as Columns and Rank as rows and dropping location column
overall_data=[rank,city_name,state,estimate_18,census,change,area_insq,area_inkm,population_insq,population_inkm,location]

## defining an function to use it 
def dataframe():
    df=pd.DataFrame()
    for i in range(len(Attributes)):
        df1=pd.DataFrame(overall_data[i],columns=[Attributes[i]])
        df=pd.concat([df,df1],axis=1)
    df=df.drop(['Location','Change'],axis=1)
    return df