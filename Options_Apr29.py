import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

Apr29 = pd.read_csv('unusual_options_29apr.csv')

Ticker = 'SPY'

Apr29['Price'] = Apr29.Volume * Apr29.Midpoint
Apr29 = Apr29.sort_values('Price', axis=0, ascending=False)
Apr29['Exp Date'] = pd.to_datetime(Apr29['Exp Date'])
SPY_Puts = Apr29.loc[(Apr29['Symbol'] == Ticker) & (Apr29['Type'] == 'Put')]
SPY_Calls = Apr29.loc[(Apr29['Symbol'] == Ticker) & (Apr29['Type'] == 'Call')]

plt.scatter(SPY_Puts.Strike, SPY_Puts['Exp Date'],
            s=SPY_Puts['Price']/max(SPY_Puts['Price'])*2000,
            alpha=0.5, c='red')
plt.scatter(SPY_Calls.Strike, SPY_Calls['Exp Date'],
            s=SPY_Calls['Price']/max(SPY_Puts['Price'])*2000,
            alpha=0.5, c='green')

# plt.xlim(265, 315)
plt.ylim(datetime.date(2020,3,15), datetime.date(2021,1,30))
# plt.xlabel('Strike Price')
# plt.ylabel('Strike Date')

plt.grid(color='grey', linestyle='-', linewidth=0.2)

