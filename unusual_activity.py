import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Enter the file name here
df = pd.read_csv('unusual_options_4may.csv')

# Choose the Ticker
Ticker = 'SPY'

# This part estimates the price of the bet
df['Price'] = df.Volume * df.Midpoint
df = df.sort_values('Price', axis=0, ascending=False)
df['Exp Date'] = pd.to_datetime(df['Exp Date'])
# purchase_time = []
# for timing in df['Time']:
#     purchase_time.append(datetime.time(int(timing[0:2]), int(timing[3:5])))
# df['Time'] = purchase_time
df_puts = df.loc[(df['Symbol'] == Ticker) & (df['Type'] == 'Put')]
df_calls = df.loc[(df['Symbol'] == Ticker) & (df['Type'] == 'Call')]

# Add time or date filters
# df_puts = df_puts.loc[(df_puts['Time'] < datetime.time(15, 30))]
# df_calls = df_calls.loc[(df_calls['Time'] < datetime.time(15, 30))]

# This is the plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Adjust the sizes color and transparency of the plot
transparency, sizing = 0.5, 2000
largest_bet = max(df.loc[(df['Symbol'] == Ticker), 'Price'])
call_color = 'green'
put_color = 'red'

plt.scatter(df_puts.Strike, df_puts['Exp Date'],
            s=df_puts['Price']/largest_bet*sizing,
            alpha=transparency, c=put_color)
plt.scatter(df_calls.Strike, df_calls['Exp Date'],
            s=df_calls['Price']/largest_bet*sizing,
            alpha=transparency, c=call_color)

# Adjust the date and range of the plot
plt.xlim(265, 300)
plt.ylim(datetime.date(2020,5,1), datetime.date(2020,5,29))
ax.set_xticks(np.arange(265, 300, 5))
plt.grid(color='grey', linestyle='-', linewidth=0.2)

