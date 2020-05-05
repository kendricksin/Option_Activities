import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Enter the file name here
df = pd.read_csv('unusual_stocks_30apr.csv')

# Choose the Ticker
Ticker = 'AAPL'

# This part estimates the price of the bet
df['Price'] = df.Volume * df.Midpoint * 100
df = df.sort_values('Price', axis=0, ascending=False)
df['Exp Date'] = pd.to_datetime(df['Exp Date'])
df_puts = df.loc[(df['Symbol'] == Ticker) & (df['Type'] == 'Put') & (df['Exp Date'] == datetime.date(2020,5,1))]
df_calls = df.loc[(df['Symbol'] == Ticker) & (df['Type'] == 'Call') & (df['Exp Date'] == datetime.date(2020,5,1))]

# This is the plot for the bet
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Adjust the sizes color and transparency of the plot
transparency, sizing = 0.5, 3000
largest_bet = max(df.loc[(df['Symbol'] == Ticker), 'Price'])
call_color = 'green'
put_color = 'red'

plt.scatter(df_puts.Strike, df_puts['Price'],
            s=df_puts['Price']/largest_bet*sizing,
            alpha=transparency, c=put_color)
plt.scatter(df_calls.Strike, df_calls['Price'],
            s=df_calls['Price']/largest_bet*sizing,
            alpha=transparency, c=call_color)

# Adjust the date and range of the plot
# plt.xlim(2200, 2800)
# plt.ylim(datetime.date(2020,4,28), datetime.date(2020,5,17))
# plt.ylabel('Strike Date')
# plt.xlabel('Strike Price')
# ax.set_xticks(np.arange(2200, 2800, 50))
plt.grid(color='grey', linestyle='-', linewidth=0.2)

