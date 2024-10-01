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
GT ID:  (replace with your GT ID)  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		 	   		  		  		    	 		 		   		 		  

  		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		 	   		  		  		    	 		 		   		 		  
from util import get_data, plot_data  		  	   		 	   		  		  		    	 		 		   		 		  
import optimize_something.optimization as opt
pd.set_option('display.max_columns', None)
pd.set_option("display.max_rows", None)
def build_prices(df):
    print('\n')
    start_date = min(df['Date'])
    end_date = max(df['Date'])
    # print(start_date, '|', end_date)
    stocks = df['Symbol'].unique()
    # start_date = dt.datetime(2011, 1, 1)
    # end_date = dt.datetime(2011, 12, 31)
    prices = get_data(stocks, pd.date_range(start_date, end_date))
    prices = prices[stocks]  # remove SPY
    prices['Cash'] = 1.00
    # print(prices)
    return prices

def build_trades(csv_df, prices, commission, impact):
    # approach 1: make a fresh df
    # stocks = csv_df.loc[:, 'Symbol'].unique()

    # trades = pd.DataFrame(index = csv_df.index, columns = stocks)
    # trades['Cash'] = 1
    # trades.fillna(0)
    # print(trades)

    # approach 2: copy an old one and clean it
    trades = prices.copy(deep=True)
    trades.iloc[:, :] = 0


    #UPDATING TRADES TABLE
    for i in range(csv_df.shape[0]):

        date, symbol, order, shares = csv_df.iloc[i, :]
        # print(date)
        # print(symbol)
        # print(order)
        # print(shares)
        # print(date, symbol, order, shares)
        price = prices.loc[date, symbol]
        # print('price of', symbol, 'is', price)
        if order == "BUY":
            #if you buy, cash goes down but shares go up
            # trades.loc[date, 'Cash'] = trades.loc[date, 'Cash'] + (-1 * (( price + (impact * price) * shares)+commission)   )
            trades.loc[date, 'Cash'] = trades.loc[date, 'Cash'] + (-1 * price * shares)
            trades.loc[date, symbol] = trades.loc[date, symbol] + shares
        else: #sell
            #if you sell, cash can go up OR down but shares go down
            # trades.loc[date, 'Cash'] = trades.loc[date, 'Cash'] + (((price - (impact * price)) * shares) - commission)
            trades.loc[date, 'Cash'] = trades.loc[date, 'Cash'] + (price*shares)
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

    # print(rows, cols)

    #day 0 case:
    holdings.iloc[0, -1] = start_val

    holdings = holdings.cumsum(axis =0) + trades.cumsum(axis=0)
    # print('holdings 2')
    # print(holdings_2)
    # print('---------')
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

    # print('values table')
    # print(values)
    # print('------------------------------------------')
    return values

def build_daytotal(values):
    # copy an old one and clean it and use it
    day_total = values.copy(deep=True)
    day_total.iloc[:, :] = 0
    day_total = values.sum(axis = 1)


    # print('day total table')
    # print(day_total)
    # print('------------------------------------------')
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
    print('\n')
    # df = pd.read_csv('./orders/orders-01.csv',  parse_dates=True, na_values = ['nan'])
    df = pd.read_csv(orders_file, parse_dates=True, na_values = ['nan'])
    df = df.sort_values(by = "Date")
    # print(df)

    prices = build_prices(df)
    trades = build_trades(df, prices, commission, impact)
    holdings = build_holdings(prices, trades, start_val)
    values = build_values(prices, holdings)

    day_total = build_daytotal(values)
    # print(day_total)
    # print('end of my code')
    return day_total



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
    print('\n')
    # print(df)
    # Process orders  		  	   		 	   		  		  		    	 		 		   		 		  
    portvals = compute_portvals(orders_file=of, start_val=sv)  		  	   		 	   		  		  		    	 		 		   		 		  
    if isinstance(portvals, pd.DataFrame):  		  	   		 	   		  		  		    	 		 		   		 		  
        portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		 	   		  		  		    	 		 		   		 		  
    else:  		  	   		 	   		  		  		    	 		 		   		 		  
        "warning, code did not return a DataFrame"
    # print(portvals)
    # Get portfolio stats  		  	   		 	   		  		  		    	 		 		   		 		  
    # Here we just fake the data. you should use your code from previous assignments.  		  	   		 	   		  		  		    	 		 		   		 		  
    start_date = min(df['Date'])
    end_date = max(df['Date'])
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio, ev, portvals =opt.assess_portfolio(
        start_date,
        end_date,
        syms = df['Symbol'].unique(),
        allocs = [.2, .2, .2, .2],
        sv = 1000000,
        rfr = 0.0,
        sf = 252.0
    )

    # print(cum_ret)

    # Compare portfolio against $SPX
    # print(f"Date Range: {start_date} to {end_date}")
    # print()
    # print(f"Sharpe Ratio of Fund: {sharpe_ratio}")
    # # print(f"Sharpe Ratio of SPY : {sharpe_ratio_SPY}")
    # print()
    # print(f"Cumulative Return of Fund: {cum_ret}")
    # # print(f"Cumulative Return of SPY : {cum_ret_SPY}")
    # print()
    # print(f"Standard Deviation of Fund: {std_daily_ret}")
    # # print(f"Standard Deviation of SPY : {std_daily_ret_SPY}")
    # print()
    # print(f"Average Daily Return of Fund: {avg_daily_ret}")
    # # print(f"Average Daily Return of SPY : {avg_daily_ret_SPY}")
    # print()
    # print(f"Final Portfolio Value: {portvals[-1]}")
  		  	   		 	   		  		  		    	 		 		   		 		  
def author():
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 	   		  		  		    	 		 		   		 		  
    """
    return "tcheng99"  # Change this to your user ID

def study_group(self):

    return 'tcheng99'

if __name__ == "__main__":  		  	   		 	   		  		  		    	 		 		   		 		  
    test_code()  		  	   		 	   		  		  		    	 		 		   		 		  


'''
# # In the template, instead of computing the value of the portfolio, we just
    # # read in the value of IBM over 6 months
    # start_date = dt.datetime(2008, 1, 1)
    # end_date = dt.datetime(2008, 6, 1)
    # portvals = get_data(["IBM", "AAPL"], pd.date_range(start_date, end_date))
    # portvals = portvals[["IBM", "AAPL"]]  # remove SPY
    # print('ibm')
    # print(portvals)
    # rv = pd.DataFrame(index=portvals.index, data=portvals.values)
  	#
    # return rv
    # return portvals
    # df = pd.read_csv('./orders/orders-01.csv')
    # orders_df = pd.read_csv(orders_file, index_col=’Date’, parse_dates = True, na_values = [‘nan’])
    # # print('\n', df.head())
    # # df.head()
    # return rv
'''
# Date,Symbol,Order,Shares


