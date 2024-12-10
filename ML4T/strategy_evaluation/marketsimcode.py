""""""
"""MC2-P1: Market simulator.  		  	   		 	   		  		  		    	 		 		   		 		  

Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 	   		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 	   		  		  		    	 		 		   		 		  

Template code for CS 4646/7646  		  	   		 	   		  		  		    	 		 		   		 		  

Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 	   		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 	   		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 	   		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   		  		  		    	 		 		   		 		  
or edited.  		  	   		 	   		  		  		    	 		 		   		 		  

We do grant permission to share solutions privately with non-students such  		  	   		 	   		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 	   		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 	   		  		  		    	 		 		   		 		  

-----do not edit anything above this line---  		  	   		 	   		  		  		    	 		 		   		 		  

Student Name: Tommy Cheng (replace with your name)  		  	   		 	   		  		  		    	 		 		   		 		  
GT User ID: tcheng99 (replace with your User ID)  		  	   		 	   		  		  		    	 		 		   		 		  
GT ID: 903967530  (replace with your GT ID)  		  	   		 	   		  		  		    	 		 		   		 		  
"""

import datetime as dt
import math

import numpy as np

import pandas as pd
from util import get_data, plot_data


def build_prices(df):

    # start_date = df.index[0]
    # end_date = df.index[-1]
    stocks = df.columns[0]

    prices = get_data([stocks], pd.date_range(df.index[0], df.index[-1]))
    prices = pd.DataFrame(prices[stocks], columns = [stocks])

    # prices = prices[stocks]  # remove SPY
    prices['Cash'] = 1.00

    return prices


def build_trades(opt_trades, prices, commission, impact, start_val):
    #Setting up trades df to include cash
    trades = prices.copy(deep=True)
    trades.iloc[:, :] = 0
    trades['Cash'] = 0

    # trades.iloc[0, 1] = start_val

    # trades['IBM'] = opt_trades
    trades.iloc[:, 0] = opt_trades
    for i in range(trades.shape[0]):
        #cash = stocks * prices of that day + (cash of today)
        # trades.loc[date, 'Cash'] + (-1 * ((( price + (impact * price)) * shares)+commission)   )
        trades.iloc[i, 1] = ((trades.iloc[i, 0] * prices.iloc[i, 0]) * -1) + trades.iloc[i, 1]


    ##creating an empty trades DF to add info to

    return trades


def build_holdings(prices, trades, start_val):

    # copy an old one and clean it and use it
    holdings = trades.copy(deep=True)
    holdings.iloc[:, :] = 0
    holdings.iloc[0, -1] = start_val
    holdings.iloc[0:, 0 ] = 0

    holdings = holdings.cumsum(axis=0) + trades.cumsum(axis=0)

    return holdings


def build_values(prices, holdings):
    ###NOTE: try df.cumsum()
    # copy an old one and clean it and use it
    values = holdings.copy(deep=True)

    values.iloc[0:, :] = 0

    # need consider day 0 case

    rows, cols = holdings.shape
    # iterate through pandas df

    for i in range(rows):
        values.iloc[i] = holdings.iloc[i] * prices.iloc[i]

    return values
    # return 1

def build_daytotal(values):
    # copy an old one and clean it and use it
    day_total = values.copy(deep=True)
    day_total.iloc[:, :] = 0
    day_total = values.sum(axis=1)

    return day_total


def compute_portvals(
        trades = pd.DataFrame([0]),
        start_val=100000,
        commission=9.95,
        impact=0.005,
):
    """
    Computes the portfolio values.
    """





    prices = build_prices(trades)

    adj_trades = build_trades(trades, prices, commission, impact, start_val)
    print(adj_trades)
    holdings = build_holdings(prices, adj_trades, start_val)

    values = build_values(prices, holdings)
    #
    day_total = build_daytotal(values)


    return day_total


def assess_portfolio(
        port_val,
        sf,
        rfr
):
    cr = (port_val.iloc[-1] / port_val.iloc[0]) - 1
    # daily returns if using port_val
    daily_returns_all = port_val.copy()
    daily_returns_all.iloc[1:] = (daily_returns_all.iloc[1:] / daily_returns_all.iloc[:-1].values) - 1
    # daily_returns_all.iloc[0] = 0
    daily_returns_all = daily_returns_all[1:]
    # 4. mean
    adr = daily_returns_all.mean()

    # 5. standard deviation
    sddr = daily_returns_all.std()

    # 6. Sharpe Ratio
    # sr = math.sqrt(sf)*(daily_returns_all.mean() - rfr/sddr)
    sr = math.sqrt(sf) * (adr - rfr) / sddr

    # Compare daily portfolio value with SPY using a normalized plot

    ev = port_val[-1]
    return cr, adr, sddr, sr, ev, port_val


def author():
    """
    :return: The GT username of the student
    :rtype: str
    """
    return "tcheng99"  # Change this to your user ID


def study_group(self):
    return 'tcheng99'

