import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Enter the file name here
df = pd.read_csv('unusual_options_30apr.csv')

# Choose the Ticker
Ticker = 'SPY'

# This part estimates the price of the bet
df['Price'] = df.Volume * df.Midpoint
df = df.sort_values('Price', axis=0, ascending=False)
df['Exp Date'] = pd.to_datetime(df['Exp Date'])
df_puts = df.loc[(df['Symbol'] == Ticker) & (df['Type'] == 'Put')]
df_calls = df.loc[(df['Symbol'] == Ticker) & (df['Type'] == 'Call')]

# This is the plot for the bet
plt.scatter(df_puts.Strike, df_puts['Exp Date'],
            s=df_puts['Price']/max(df_puts['Price'])*2000,
            alpha=0.5, c='red')
plt.scatter(df_calls.Strike, df_calls['Exp Date'],
            s=df_calls['Price']/max(df_puts['Price'])*2000,
            alpha=0.5, c='green')

# Adjust the limits
plt.xlim(265, 315)
plt.ylim(datetime.date(2020,4,15), datetime.date(2020,6,30))
# plt.xlabel('Strike Price')
# plt.ylabel('Strike Date')
plt.grid(color='grey', linestyle='-', linewidth=0.2)

