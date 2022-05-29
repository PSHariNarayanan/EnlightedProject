# -*- coding: utf-8 -*-
"""
Version : 01
Description : This script takes data point,timestamp,receiver Ids as input and
provides top 5 spatial or temporal points where max receiver Ids are available
@author: Hari
"""

import pandas as pd

# Declare variables
file_path = r"C:\Users\user\Downloads\dataset2.csv"
ID_col = "ID"
loc_col = "Location"
time_col = "Timestamp"
rcv_count = "Receiver_Count"
top_n_points = 5
spa_or_temp = 'Spatial'

# Read file data
data = pd.read_csv(file_path)
data.Timestamp = pd.to_datetime(data.Timestamp)
print("Shape of dataframe is :",data.shape)


def ReceiverCount(df,ID_col,ST_col,
                  rcv_count,top_n_points) :
    # Filter spatial/temporal data
    df1 = df[[ID_col,ST_col]]
    
    # Group based on Location/Spatial data ,take count and pick top n points
    grouped_df = df1.groupby(ST_col).count().reset_index()
    grouped_df.columns = [ST_col,rcv_count]
    sorted_df = grouped_df.sort_values([rcv_count],ascending=False).reset_index(drop=True)
    final_df = sorted_df[:top_n_points]
    return final_df

if spa_or_temp =='Spatial' :
    final_data = ReceiverCount(data, ID_col, loc_col, rcv_count, 
                               top_n_points)
    print("Top {} spatial points where maximum receivers present are :".format(top_n_points))
    print(final_data)
elif spa_or_temp == 'Temporal' :
    final_data = ReceiverCount(data, ID_col, time_col, rcv_count, 
                               top_n_points)
    print("Top {} temporal points where maximum receivers present are :".format(top_n_points))
    print(final_data)
else :
    print("Kindly choose between either 'Spatial' or 'Temporal'")
    