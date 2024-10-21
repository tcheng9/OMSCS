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

    start_date = min(df['Date'])
    end_date = max(df['Date'])

    stocks = df['Symbol'].unique()
    # start_date = dt.datetime(2011, 1, 1)
    # end_date = dt.datetime(2011, 12, 31)
    prices = get_data(stocks, pd.date_range(start_date, end_date))
    prices = prices[stocks]  # remove SPY
    prices['Cash'] = 1.00

    return prices

def build_trades(csv_df, prices, commission, impact):
    # approach 1: make a fresh df
    # stocks = csv_df.loc[:, 'Symbol'].unique()

    # trades = pd.DataFrame(index = csv_df.index, columns = stocks)
    # trades['Cash'] = 1
    # trades.fillna(0)

    # approach 2: copy an old one and clean it
    trades = prices.copy(deep=True)
    trades.iloc[:, :] = 0
    print('\n')
    # print(csv_df)

    #UPDATING TRADES TABLE
    for i in range(csv_df.shape[0]):

        date, symbol, order, shares = csv_df.iloc[i, :]

        price = prices.loc[date, symbol]

        if order == "BUY":
            #if you buy, cash goes down but shares go up
            trades.loc[date, 'Cash'] = trades.loc[date, 'Cash'] + (-1 * ((( price + (impact * price)) * shares)+commission)   )
            # trades.loc[date, 'Cash'] = trades.loc[date, 'Cash'] + (-1 * price * shares)
            trades.loc[date, symbol] = trades.loc[date, symbol] + shares
        else: #sell
            #if you sell, cash can go up OR down but shares go down
            trades.loc[date, 'Cash'] = trades.loc[date, 'Cash'] + (((price - (impact * price)) * shares) - commission)
            # trades.loc[date, 'Cash'] = trades.loc[date, 'Cash'] + (price*shares)
            trades.loc[date, symbol] = trades.loc[date, symbol] + (-1*shares)

    ##creating an empty trades DF to add info to
    print(trades)
    return trades

def build_holdings(prices, trades, start_val):
    # copy an old one and clean it and use it
    holdings = trades.copy(deep=True)
    holdings.iloc[:, :] = 0

    #build holdings table

    # holdings.loc[:, 'AAPL'] = trades.loc[:, 'AAPL']


    #day 0 case:
    holdings.iloc[0, -1] = start_val

    holdings = holdings.cumsum(axis =0) + trades.cumsum(axis=0)
    print(holdings)
    #day 1 - end case;


    return holdings

def build_values(prices, holdings):
    ###NOTE: try df.cumsum()
    # copy an old one and clean it and use it
    values = prices.copy(deep=True)
    values.iloc[:, :] = 0

    #need consider day 0 case

    rows, cols = holdings.shape
    #iterate through pandas df
    for r in range(rows):
        for c in range(cols):
            values.iloc[r, c] = holdings.iloc[r, c] * prices.iloc[r, c]


    return values

def build_daytotal(values):
    # copy an old one and clean it and use it
    day_total = values.copy(deep=True)
    day_total.iloc[:, :] = 0
    day_total = values.sum(axis = 1)



    return day_total


def compute_portvals(  		  	   		 	   		  		  		    	 		 		   		 		  
    orders_file="./orders/orders.csv",  		  	   		 	   		  		  		    	 		 		   		 		  
    start_val=1000000,  		  	   		 	   		  		  		    	 		 		   		 		  
    commission=9.95,  		  	   		 	   		  		  		    	 		 		   		 		  
    impact=0.005,  		  	   		 	   		  		  		    	 		 		   		 		  
):  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    Computes the portfolio values.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    :param orders_file: Path of the order file or the file object  		  	   		 	   		  		  		    	 		 		   		 		  
    :type orders_file: str or file object  		  	   		 	   		  		  		    	 		 		   		 		  
    :param start_val: The starting value of the portfolio  		  	   		 	   		  		  		    	 		 		   		 		  
    :type start_val: int  		  	   		 	   		  		  		    	 		 		   		 		  
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		 	   		  		  		    	 		 		   		 		  
    :type commission: float  		  	   		 	   		  		  		    	 		 		   		 		  
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		 	   		  		  		    	 		 		   		 		  
    :type impact: float  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: pandas.DataFrame  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    # this is the function the autograder will call to test your code  		  	   		 	   		  		  		    	 		 		   		 		  
    # NOTE: orders_file may be a string, or it may be a file object. Your  		  	   		 	   		  		  		    	 		 		   		 		  
    # code should work correctly with either input


    # TODO: Your code here

    # df = pd.read_csv('./orders/orders-01.csv',  parse_dates=True, na_values = ['nan'])
    df = pd.read_csv(orders_file, parse_dates=True, na_values = ['nan'])
    df = df.sort_values(by = "Date")


    prices = build_prices(df)
    trades = build_trades(df, prices, commission, impact)
    holdings = build_holdings(prices, trades, start_val)
    values = build_values(prices, holdings)

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
    return cr, adr, sddr, sr, ev,port_val


def test_code():
    """
    Helper function to test code
    """
    # this is a helper function you can use to test your code
    # note that during autograding his function will not be called.
    # Define input parameters

    of = "./orders/orders-01.csv"
    sv = 1000000
    df = pd.read_csv(of)

    # Process orders
    portvals = compute_portvals(orders_file=of, start_val=sv, commission= 0.0, impact=0.0)
    if isinstance(portvals, pd.DataFrame):
        portvals = portvals[portvals.columns[0]]  # just get the first column
    else:
        "warning, code did not return a DataFrame"

    # Get portfolio stats
    # Here we just fake the data. you should use your code from previous assignments.
    start_date = min(df['Date'])
    end_date = max(df['Date'])




    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio, ev, portvals =assess_portfolio(
        portvals,
        rfr = 0.0,
        sf = 252.0
    )


  		  	   		 	   		  		  		    	 		 		   		 		  
def author():
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 	   		  		  		    	 		 		   		 		  
    """
    return "tcheng99"  # Change this to your user ID

def study_group(self):

    return 'tcheng99'


