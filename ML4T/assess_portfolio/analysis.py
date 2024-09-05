"""Analyze a portfolio.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Copyright 2017, Georgia Tech Research Corporation  		  	   		 	   		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332-0415  		  	   		 	   		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	   		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt
import pandas as pd  		  	   		 	   		  		  		    	 		 		   		 		  
from util import get_data, plot_data  		  	   		 	   		  		  		    	 		 		   		 		  
import math
  		  	   		 	   		  		  		    	 		 		   		 		  
# This is the function that will be tested by the autograder  		  	   		 	   		  		  		    	 		 		   		 		  
# The student must update this code to properly implement the functionality  		  	   		 	   		  		  		    	 		 		   		 		  
def assess_portfolio(  		  	   		 	   		  		  		    	 		 		   		 		  
    sd=dt.datetime(2008, 1, 1),  		  	   		 	   		  		  		    	 		 		   		 		  
    ed=dt.datetime(2009, 1, 1),  		  	   		 	   		  		  		    	 		 		   		 		  
    syms=["GOOG", "AAPL", "GLD", "XOM"],  		  	   		 	   		  		  		    	 		 		   		 		  
    allocs=[0.1, 0.2, 0.3, 0.4],  		  	   		 	   		  		  		    	 		 		   		 		  
    sv=1000000,  		  	   		 	   		  		  		    	 		 		   		 		  
    rfr=0.0,  		  	   		 	   		  		  		    	 		 		   		 		  
    sf=252.0,  		  	   		 	   		  		  		    	 		 		   		 		  
    gen_plot=False,
):  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    Estimate a set of test points given the model we built.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   		  		  		    	 		 		   		 		  
    :type sd: datetime  		  	   		 	   		  		  		    	 		 		   		 		  
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   		  		  		    	 		 		   		 		  
    :type ed: datetime  		  	   		 	   		  		  		    	 		 		   		 		  
    :param syms: A list of 2 or more symbols that make up the portfolio (note that your code should support any symbol in the data directory)  		  	   		 	   		  		  		    	 		 		   		 		  
    :type syms: list  		  	   		 	   		  		  		    	 		 		   		 		  
    :param allocs:  A list of 2 or more allocations to the stocks, must sum to 1.0  		  	   		 	   		  		  		    	 		 		   		 		  
    :type allocs: list  		  	   		 	   		  		  		    	 		 		   		 		  
    :param sv: The starting value of the portfolio  		  	   		 	   		  		  		    	 		 		   		 		  
    :type sv: int  		  	   		 	   		  		  		    	 		 		   		 		  
    :param rfr: The risk free return per sample period that does not change for the entire date range (a single number, not an array)  		  	   		 	   		  		  		    	 		 		   		 		  
    :type rfr: float  		  	   		 	   		  		  		    	 		 		   		 		  
    :param sf: Sampling frequency per year  		  	   		 	   		  		  		    	 		 		   		 		  
    :type sf: float  		  	   		 	   		  		  		    	 		 		   		 		  
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		 	   		  		  		    	 		 		   		 		  
        code with gen_plot = False.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type gen_plot: bool  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: A tuple containing the cumulative return, average daily returns,  		  	   		 	   		  		  		    	 		 		   		 		  
        standard deviation of daily returns, Sharpe ratio and end value  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: tuple  		  	   		 	   		  		  		    	 		 		   		 		  
    """

    '''
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    ERASE PRINT SETTINGS LATER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
    print('\n')
    # pd.options.display.float_format = '{:.0f}'.format



    # Read in adjusted closing prices for given symbols, date range
    dates = pd.date_range(sd, ed)
    prices_all = get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms]  # only portfolio symbols
    # prices = list(prices_all.columns.values)
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later

    # Get daily portfolio value

    # Get portfolio statistics (note: std_daily_ret = volatility)

    '''
    -----------CALCULATING DAILY PORTFOLIO VALUE----------
    '''
    # print(prices_all)
    normed = prices/prices.iloc[0].values
    alloced = normed * allocs
    pos_vals = alloced * sv
    port_val = pos_vals.sum(axis = 1) #daily portfolio value
    cr = (port_val.iloc[-1] / port_val.iloc[0]) - 1

    '''
    -------------GETTING PORTFOLIO STATISTICS----------
    Steps:
    1. Geet data for specific stores
    2. Get daily portfolio values
    3. Get portfolio statistics
    '''
    # Daily returns if using prices of stocks
    # daily_returns_all = prices_all.copy()
    # daily_returns_all.iloc[1:] = (daily_returns_all.iloc[1:]/daily_returns_all.iloc[:-1].values) -1
    # # daily_returns_all.iloc[0] = 0
    # daily_returns_all = daily_returns_all[1:]
    # print(daily_returns_all)

    #daily returns if using port_val
    daily_returns_all = port_val.copy()
    daily_returns_all.iloc[1:] = (daily_returns_all.iloc[1:] / daily_returns_all.iloc[:-1].values) - 1
    # daily_returns_all.iloc[0] = 0
    daily_returns_all = daily_returns_all[1:]
    #4. mean
    adr = daily_returns_all.mean()

    #5. standard deviation
    sddr = daily_returns_all.std()

    #6. Sharpe Ratio
    # sr = math.sqrt(sf)*(daily_returns_all.mean() - rfr/sddr)
    sr = math.sqrt(sf) * (adr-rfr)/sddr

    # Compare daily portfolio value with SPY using a normalized plot
    if gen_plot:  		  	   		 	   		  		  		    	 		 		   		 		  
        # add code to plot here  		  	   		 	   		  		  		    	 		 		   		 		  
        df_temp = pd.concat(  		  	   		 	   		  		  		    	 		 		   		 		  
            [port_val, prices_SPY], keys=["Portfolio", "SPY"], axis=1
        )
        # plt.plot(df_temp)
        # plt.show()
        pass
  		  	   		 	   		  		  		    	 		 		   		 		  
    # Add code here to properly compute end value  		  	   		 	   		  		  		    	 		 		   		 		  
    # cr = 10
    # adr = 110
    # sddr = 110
    # sr = 110
    # ev = 110
    ev = port_val[-1]
    return cr, adr, sddr, sr, ev
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
def test_code():  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    Performs a test of your code and prints the results  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    # This code WILL NOT be tested by the auto grader  		  	   		 	   		  		  		    	 		 		   		 		  
    # It is only here to help you set up and test your code  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    # Define input parameters  		  	   		 	   		  		  		    	 		 		   		 		  
    # Note that ALL of these values will be set to different values by  		  	   		 	   		  		  		    	 		 		   		 		  
    # the autograder!  		  	   		 	   		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2009, 1, 1)  		  	   		 	   		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2010, 1, 1)  		  	   		 	   		  		  		    	 		 		   		 		  
    symbols = ["GOOG", "AAPL", "GLD", "XOM"]  		  	   		 	   		  		  		    	 		 		   		 		  
    allocations = [0.2, 0.3, 0.4, 0.1]  		  	   		 	   		  		  		    	 		 		   		 		  
    start_val = 1000000  		  	   		 	   		  		  		    	 		 		   		 		  
    risk_free_rate = 0.0  		  	   		 	   		  		  		    	 		 		   		 		  
    sample_freq = 252  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    # Assess the portfolio  		  	   		 	   		  		  		    	 		 		   		 		  
    cr, adr, sddr, sr, ev = assess_portfolio(  		  	   		 	   		  		  		    	 		 		   		 		  
        sd=start_date,  		  	   		 	   		  		  		    	 		 		   		 		  
        ed=end_date,  		  	   		 	   		  		  		    	 		 		   		 		  
        syms=symbols,  		  	   		 	   		  		  		    	 		 		   		 		  
        allocs=allocations,  		  	   		 	   		  		  		    	 		 		   		 		  
        sv=start_val,  		  	   		 	   		  		  		    	 		 		   		 		  
        gen_plot=False,
    )  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    # Print statistics  		  	   		 	   		  		  		    	 		 		   		 		  
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print(f"Symbols: {symbols}")
    print(f"Allocations: {allocations}")
    print(f"Sharpe Ratio: {sr}")
    print(f"Volatility (stdev of daily returns): {sddr}")
    print(f"Average Daily Return: {adr}")
    print(f"Cumulative Return: {cr}")
  	#
  		  	   		 	   		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		 	   		  		  		    	 		 		   		 		  
    test_code()  		  	   		 	   		  		  		    	 		 		   		 		  
