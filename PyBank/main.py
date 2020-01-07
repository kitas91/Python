#import proper libraries
import numpy as np
import pandas as pd

#create csv paths and import data into vsc
data = pd.read_csv('PyBank_data.csv', index_col="Date")
#set column as "Profit/Losses"
columns = ["Profit/Losses"]
data.columns = columns

#test data, make sure you are importing using .head or .tail
data.tail(10)

#calculating the daily percent change - How do I commit this command to add the column permanently on my dataframe? 
percent_change = data.pct_change()
percent_change.tail()

#adding % change to the table as the third entry
data["% chg"] = percent_change
data.tail()

#check your data - rounded to the second decimal
round(data.describe(), 2)

#Checking data quality - nulls - first null on %chng is natural
data.index.dtype()
data.isnull()
data.isnull().sum()
data.isnull().mean()*100

#Checking data quality - duplicate rows
data.duplicated()

#converting Profit/Losses column into floats
data['Profit/Losses'] = data['Profit/Losses'].astype('float')
data['% chng'] = data['% chng'].astype('float')
data.dtypes

#check data consistency 
print ("\n")
print (round(df.describe(), 2))


#creating variables max increase of percentage 
max_percent_increase = data.max()[1]
percent_chg_max = data.loc[data['% chg'] == max_percent_increase]

#creating variable max decrease of percentage
max_percent_decrease = data.min()[1]
percent_chg_min = data.loc[data['% chg'] == max_percent_decrease]

#creating values for requested variables
total_months = df.count()
total_pnl = df.sum()
max_increase = df.max()

#mean_change = data.mean()
#max_increase = data.max()
#min_decrease = data.min()

print ("\n")
print ("Financial Analysis: \n --------------------")
print (f"Total Months: {total_months[0]}")
print (f"Total PnL: {total_pnl [0]}")
#print (f"Average Change: {mean_change [0]}")
#print (f"Greatest Increase in Profits: {max_increase [0]}")
#print (f"Greatest Decrease in Profits: {min_decrease [0]}")


