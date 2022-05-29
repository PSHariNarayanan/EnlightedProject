# -*- coding: utf-8 -*-
"""
Version : 02
Description : This script synthesizes data points,receiver Ids as input and
provides top 5 spatial points where max receiver Ids are available
@author: Hari
"""

import pandas as pd
import random

# Declare variables
min_range = 0
max_range = 5000
sampling = 1000
ID_col = "ID"
loc_col = "Location"
rcv_count = "Receiver_Count"
top_n_points = 5

def ReceiverCount(min_range,max_range,sampling,ID_col,
                  loc_col,rcv_count,top_n_points) : 
    # Generate unique ID sequence
    receivers_id = [i for i in range(1,sampling+1)]
    
    # Generate random data points 
    x = random.sample(range(min_range,max_range),sampling)
    y = random.sample(range(min_range,max_range),sampling)
    
    # Create tuples/pairs of data points
    loc = []
    for i,j in zip(x,y):
        loc.append((i,j))
    
    # Assign same data points to different receiver IDs for Demo purpose
    loc[50:60],loc[170:180],loc[700:710] = loc[-10:],loc[-10:],loc[-10:]
    loc[54],loc[176],loc[703] = loc[-6],loc[-6],loc[-6]
    loc[57] = loc[-8]
    
    # Create dataframe, group based on Location/datapoint ,
    #                                          take count and pick top n points
    auto_df = pd.DataFrame({ID_col:receivers_id,loc_col:loc})
    print("Shape of dataframe is :",df.shape)
    grouped_df = auto_df.groupby([loc_col]).count().reset_index()
    grouped_df.columns = [loc_col,rcv_count]
    sorted_df = grouped_df.sort_values([rcv_count],ascending=False).reset_index(drop=True)
    
    final_df = sorted_df[:top_n_points]
    return final_df

final_data = ReceiverCount(min_range,max_range,sampling,ID_col,
                  loc_col,rcv_count,top_n_points)
print("Top {} data points where maximum receivers present are :".format(top_n_points))
print(final_data)