
import pandas as pd
import datetime as dt
import math

import numpy as np

import pandas as pd
from util import get_data, plot_data
import matplotlib.pyplot as plt
pd.set_option('display.max_row', None)

def testPolicy(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000):
    print('placeholder')
    print('\n')
    prices = get_data([symbol], pd.date_range(sd, ed))
    prices = prices[symbol]  # remove SPY
    # prices['Cash'] = 1.00
    # print(prices)

    trades = prices.copy()
    trades.iloc[0:] = 0

    current_holdings = 0

    for i in range(prices.shape[0]-1):
        today = prices.iloc[i]
        tomorrow = prices.iloc[i+1]
        # print(today, 'vs', tomorrow)
        if tomorrow > today:
            # price will go up
            # print('price up')
            if current_holdings == 1000:

                #already holding stocks long and dont want to short
                trades.iloc[i] = 0
            elif current_holdings == 0:

                #want to buy stocks long but not short
                trades.iloc[i] = 1000
                current_holdings += 1000
            else:
                #current holdings = -1000

                #want to sell all long stocks and short stock
                trades.iloc[i] = 2000
                current_holdings += 2000
        elif tomorrow < today:
            # print('price down')
            # price will go down
            if current_holdings == 1000:

                #want to sell all stocks and short
                trades.iloc[i] = -2000
                current_holdings -= 2000
            elif current_holdings == 0:

                #want to short stock and not buy long
                trades.iloc[i] = 1000
                current_holdings -= 1000
            else:

                #you are at -1000 holdings
                #you don't wnat to buy long, can't short anymore -> do nothing
                trades.iloc[i] = 0
        else:
            # print('price stays the exact same')
            trades.iloc[i] = 0
        print(current_holdings)



    print(trades)
    return trades



def author():
    """
    :return: The GT username of the student
    :rtype: str
    """
    return "tcheng99"  # Change this to your user ID


def study_group(self):
    return 'tcheng99'


if __name__ == "__main__":
    testPolicy()

