import numpy as np
import pandas as pd
import os
import csv 

df = pd.read_csv('PyBank_data.csv', index_col= 'Date')

total_months = df.count()
total_pnl = df.sum(axis = 0, skipna = True)
mean_change = df.mean()
max_increase = df.max()
min_decrease = df.min()

print ("Financial Analysis: \n --------------")
print (f"Total Months: {total_months[0]}")
print (f"Total PnL: {total_pnl [0]}")
print (f"Average Change: {mean_change [0]}")
print (f"Greatest Increase in Profits: {max_increase [0]}")
print (f"Greatest Decrease in Profits: {min_decrease [0]}")

