# Import proper libraries
import numpy as np
import pandas as pd

# Create csv paths and import data into vsc
data = pd.read_csv('PyBank_data.csv', index_col="Date")
# Set column as "Profit/Losses"
columns = ["Profit/Losses"]
data.columns = columns

# Test data, make sure you are importing using .head or .tail
data.tail()

# Create an Incrase/Decrease column 
data["Increase/Decrease"] = data['Profit/Losses'] - data['Profit/Losses'].shift()

# Creating a daily percent change column 
data["percent_chg"] = data['Profit/Losses'].pct_change()

# Check new dataframe
data.tail()

# Checking data quality - nulls - first null on %chng is natural
data.isnull()
data.isnull().sum()
data.isnull().mean()*100

# Checking data quality - duplicate rows
data.duplicated()

# Converting Profit/Losses, Increase/Decrease, Percent_change column into floats
data['Profit/Losses'] = data['Profit/Losses'].astype('float')
data['Increase/Decrease'] = data['Increase/Decrease'].astype('float')
data['percent_chg'] = data['percent_chg'].astype('float')

# Check your data - rounded to the second decimal
round(data.describe(), 2)


# Creating variables max increase of Increase/Decrease 
max_increase = data.max()[1]
max_inc_dec = data.loc[data['Increase/Decrease'] == max_increase]

# Creating variables max increase of Increase/Decrease 
min_increase = data.min()[1]
min_inc_dec = data.loc[data['Increase/Decrease'] == min_increase]

# Creating variable average change of Increase/Decrease 
average_mean = data.mean()[1]

# Creating values for requested variables
total_months = data.count()
total_pnl = data.sum()

print ("\n")
print ("Financial Analysis: \n--------------------")
print (f"Total Months: {total_months[0]}")
print (f"Total PnL: {total_pnl [0]}")
print (f"Average Change: {average_mean}")
print (f"Greatest Increase in Profits: {max_inc_dec.index[0]} {max_inc_dec.iloc[0,1]}")
print (f"Greatest Decrease in Profits: {min_inc_dec.index[0]} {min_inc_dec.iloc[0,1]}")