# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:46:44 2019

@author: udayjuttu
"""
from pandas.io import gbq
from City_index import aggregated_dataframe
final_df=aggregated_dataframe()
final_df.fillna(0,inplace=True)

#Download to csv
final_df.to_csv(r'path.csv',index=False, encoding='utf-8')

# directly importing to gb destimation_table='table_Schema.destimation_table'
#project_id='project_id'
#executing this will open Bigquery login page in google.

final_df.to_gbq(destination_table='test.city_data',project_id='workbench-201924', if_exists='replace')