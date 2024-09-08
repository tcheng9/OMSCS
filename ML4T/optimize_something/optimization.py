""""""  		  	   		 	   		  		  		    	 		 		   		 		  
"""MC1-P2: Optimize a portfolio.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
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
GT ID: 903967530 (replace with your GT ID)  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt  		  	   		 	   		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		 	   		  		  		    	 		 		   		 		  
from util import get_data, plot_data
import math
import scipy.optimize as spo

def author():
    """
    :return: The GT username of the student
    :rtype: str
    """
    return "tcheng99"  # replace tb34 with your Georgia Tech username.


def study_group():
    return "tcheng99"
# spo.minimize(calc_sr, allocs, args = ((dt.datetime(2008, 1, 1),
#  dt.datetime(2009, 1, 1),
# ["GOOG", "AAPL", "GLD", "XOM"],
# 1000000,
# 0.0,
# 252.0)))
#
# (dt.datetime(2008, 1, 1),
#  dt.datetime(2009, 1, 1),
# ["GOOG", "AAPL", "GLD", "XOM"],
# 1000000,
# 0.0,
# 252.0)

# spo.minimize(calc_sr, allocs, args = (sd, ed, syms, sv, rfr, sf))




def calc_sr(
    allocs = [0.2, 0.2, 0.2, 0.2, 0.2],
    sd=dt.datetime(2008, 1, 1),
    ed=dt.datetime(2009, 1, 1),
    syms=["GOOG", "AAPL", "GLD", "XOM"],
    sv=1000000,
    rfr=0.0,
    sf=252.0,
):
    #STEP 1: GETTING ALL DATA
    # Read in adjusted closing prices for given symbols, date range


    dates = pd.date_range(sd, ed)
    prices_all = get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms]  # only portfolio symbols
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later


    '''
    -----------CALCULATING DAILY PORTFOLIO VALUE----------
    '''
    # print(prices_all)
    normed = prices / prices.iloc[0].values
    alloced = normed * allocs
    pos_vals = alloced * sv
    port_val = pos_vals.sum(axis=1)  # daily portfolio value
    cr = (port_val.iloc[-1] / port_val.iloc[0]) - 1

    '''
    ----------GETTING PORTFOLIO STATISTICS ------------------
    '''
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
    sr = (math.sqrt(sf) * (adr - rfr) / sddr ) * -1
    ev = port_val[-1]


    # print('cr is', cr)
    # print('adr is', adr)
    # print('sddr is', sddr)
    # print('sr is', sr * -1)
    # print('ev is', ev)

    # print(sr*-1)
    return sr


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
    normed = prices / prices.iloc[0].values
    alloced = normed * allocs
    pos_vals = alloced * sv
    port_val = pos_vals.sum(axis=1)  # daily portfolio value

    cr = (port_val.iloc[-1] / port_val.iloc[0]) - 1

    '''
    -------------GETTING PORTFOLIO STATISTICS----------
    Steps:
    1. Geet data for specific stores
    2. Get daily portfolio values
    3. Get portfolio statistics
    '''


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
    if gen_plot:
        # add code to plot here
        df_temp = pd.concat(
            [port_val, prices_SPY], keys=["Portfolio", "SPY"], axis=1
        )
        # plt.plot(df_temp)
        # plt.show()
        pass

    ev = port_val[-1]
    return cr, adr, sddr, sr, ev,port_val



# This is the function that will be tested by the autograder
# The student must update this code to properly implement the functionality  		  	   		 	   		  		  		    	 		 		   		 		  
def optimize_portfolio(  		  	   		 	   		  		  		    	 		 		   		 		  
    sd=dt.datetime(2008, 1, 1),  		  	   		 	   		  		  		    	 		 		   		 		  
    ed=dt.datetime(2009, 1, 1),  		  	   		 	   		  		  		    	 		 		   		 		  
    syms=["GOOG", "AAPL", "GLD", "XOM"],  		  	   		 	   		  		  		    	 		 		   		 		  
    gen_plot=False,  		  	   		 	   		  		  		    	 		 		   		 		  
):  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    This function should find the optimal allocations for a given set of stocks. You should optimize for maximum Sharpe  		  	   		 	   		  		  		    	 		 		   		 		  
    Ratio. The function should accept as input a list of symbols as well as start and end dates and return a list of  		  	   		 	   		  		  		    	 		 		   		 		  
    floats (as a one-dimensional numpy array) that represents the allocations to each of the equities. You can take  		  	   		 	   		  		  		    	 		 		   		 		  
    advantage of routines developed in the optional assess portfolio project to compute daily portfolio value and  		  	   		 	   		  		  		    	 		 		   		 		  
    statistics.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   		  		  		    	 		 		   		 		  
    :type sd: datetime  		  	   		 	   		  		  		    	 		 		   		 		  
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   		  		  		    	 		 		   		 		  
    :type ed: datetime  		  	   		 	   		  		  		    	 		 		   		 		  
    :param syms: A list of symbols that make up the portfolio (note that your code should support any  		  	   		 	   		  		  		    	 		 		   		 		  
        symbol in the data directory)  		  	   		 	   		  		  		    	 		 		   		 		  
    :type syms: list  		  	   		 	   		  		  		    	 		 		   		 		  
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		 	   		  		  		    	 		 		   		 		  
        code with gen_plot = False.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type gen_plot: bool  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: A tuple containing the portfolio allocations, cumulative return, average daily returns,  		  	   		 	   		  		  		    	 		 		   		 		  
        standard deviation of daily returns, and Sharpe ratio  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: tuple  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    print('\n')

    # Read in adjusted closing prices for given symbols, date range
    dates = pd.date_range(sd, ed)
    prices_all = get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms]  # only portfolio symbols
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later
    # port_val = prices_SPY


    # normed_SPY = prices_SPY / prices_SPY.iloc[0].values
    # normed


    # Get daily portfolio value


    #optimizer
    allocs = [.2/len(syms)] * len(syms)
    init_bounds = (0, 1)
    bds = ((init_bounds,) * len(allocs))
    # print(bds)
    constraint1 = {'type': 'eq', 'fun': lambda inputs: 1-np.sum(allocs) }
    # bds = (0,1) * len(allocs)
    best_result = spo.minimize(calc_sr, allocs, args=(sd, ed, syms, 1000000, 0, 252),
        options = {'disp':False},
        bounds = bds,
        constraints = ({'type': 'eq', 'fun': lambda allocs: 1.0 - np.sum(allocs)})
    )
    # print(np.sum(best_result.x))
    best_allocs = best_result.x
    '''
    constraints: sum of allocs need to equal to 1
    '''
    # print('here')
    cr, adr, sddr, sr, ev, port_val = assess_portfolio(sd, ed, syms, best_allocs, 1000000, 0, 252, False)



    '''
    Trying to get graph right
    '''
    '''
       -----------CALCULATING DAILY PORTFOLIO VALUE----------
       '''
    # print(prices_all)
    sv = 1000000
    normed = prices / prices.iloc[0].values
    alloced = normed * best_allocs
    pos_vals = alloced * sv
    port_val = pos_vals.sum(axis=1)  # daily portfolio value

    # Read in adjusted closing prices for given symbols, date range
    dates = pd.date_range(sd, ed)
    prices_all = get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms]  # only portfolio symbols
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later
    # port_val = prices_SPY

    ########## SPY
    prices_SPY = prices_SPY[1:]/prices_SPY[0]
    # print(prices_SPY)

    #portfolio value
    print(port_val)
    port_val = port_val[1:]/port_val[0]
    # print(cr, adr, sddr, sr,ev)
    # Compare daily portfolio value with SPY using a normalized plot  		  	   		 	   		  		  		    	 		 		   		 		  
    if gen_plot:
        # add code to plot here
        # df_temp = pd.concat(
        #     [port_val, prices_SPY], keys=["Portfolio", "SPY"], axis=1
        # )
        # df_temp.plot()
        plt.plot(port_val, label="portfolio")
        plt.plot(prices_SPY, label = "SPY")

        # print(cr)
        plt.legend()
        plt.show()
        pass


    # allocs = [0]
    # cr = 1
    # adr = 1
    # sddr = 1
    # sr = 1
    # print('best allocs is', best_allocs)
    # print('best cr is', cr)
    # print('best adr', adr)
    # print('best sddr', sddr)
    # print('best sr', sr)



    return best_allocs, cr, adr, sddr, sr
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
def test_code():  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    This function WILL NOT be called by the auto grader.  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2008, 6, 1)
    end_date = dt.datetime(2009,6, 1)
    symbols = ['IBM', 'X', 'GLD', 'JPM']
  		  	   		 	   		  		  		    	 		 		   		 		  
    # Assess the portfolio  		  	   		 	   		  		  		    	 		 		   		 		  
    allocations, cr, adr, sddr, sr = optimize_portfolio(  		  	   		 	   		  		  		    	 		 		   		 		  
        sd=start_date, ed=end_date, syms=symbols, gen_plot=True
    )  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    # Print statistics  		  	   		 	   		  		  		    	 		 		   		 		  
    # print(f"Start Date: {start_date}")
    # print(f"End Date: {end_date}")
    # print(f"Symbols: {symbols}")
    # print(f"Allocations:{allocations}")
    # print(f"Sharpe Ratio: {sr}")
    # print(f"Volatility (stdev of daily returns): {sddr}")
    # print(f"Average Daily Return: {adr}")
    # print(f"Cumulative Return: {cr}")
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		 	   		  		  		    	 		 		   		 		  
    # This code WILL NOT be called by the auto grader  		  	   		 	   		  		  		    	 		 		   		 		  
    # Do not assume that it will be called  		  	   		 	   		  		  		    	 		 		   		 		  
    test_code()  		  	   		 	   		  		  		    	 		 		   		 		  



