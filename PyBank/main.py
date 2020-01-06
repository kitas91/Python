#import proper libraries
import numpy as np
import pandas as pd

#create csv paths and import data into vsc
data = pd.read_csv('PyBank_data.csv', index_col="Date")
columns = ["Profit/Losses"]

#test data, make sure you are importing using .head or .tail
data.tail(10)

#calculating the daily percent change
percent_change = data.pct_change()
percent_change.tail(10)

#adding % change to the table as the third entry
data["% chg"] = percent_change
data.tail()

#Checking data quality - nulls - first null on %chng is natural
print (data.index.dtype)
print (data.isnull())
print (data.isnull().sum())
print (data.isnull().mean()*100)

#Checking data quality - duplicate rows
data.duplicated()

#converting Profit/Losses column into floats
data['Profit/Losses'] = data['Profit/Losses'].astype('float')
df.dtypes

#check data consistency 
print ("\n")
print (round(df.describe(), 2))

total_months = df.count()
total_pnl = df.sum()
max_increase = df.max()

