""""""
"""  		  	   		 	   		  		  		    	 		 		   		 		  
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		 	   		  		  		    	 		 		   		 		  

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
import random

import pandas as pd
import util as ut
import BagLearner as bl
import DTLearner as dtl
import RTLearner as rtl

import marketsimcode
import indicators as inds
pd.set_option('display.max_rows', 500)


class ManualStrategy(object):
    """
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.

    :param verbose: If “verbose” is True, your code can print out information for debugging.
        If verbose = False your code should not generate ANY output.
    :type verbose: bool
    :param impact: The market impact of each transaction, defaults to 0.0
    :type impact: float
    :param commission: The commission amount charged, defaults to 0.0
    :type commission: float
    """

    # constructor
    def __init__(self, verbose=False, impact=0.0, commission=0.0):
        """
        Constructor method
        """
        self.verbose = verbose
        self.impact = impact
        self.commission = commission

        # this method should create a QLearner, and train it for trading

    def add_evidence(
            self,
            symbol="JPM",
            sd=dt.datetime(2009, 1, 1, 0, 0),
            ed=dt.datetime(2010, 1, 1, 0, 0),
            sv=100000,
            commission=9.95,
            impact=0.005
    ):
        """
        Trains your strategy learner over a given time frame.

        :param symbol: The stock symbol to train on
        :type symbol: str
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008
        :type sd: datetime
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009
        :type ed: datetime
        :param sv: The starting value of the portfolio
        :type sv: int
        """

        # add your code to do learning here

        # # example usage of the old backward compatible util function
        # syms = [symbol]
        # dates = pd.date_range(sd, ed)
        # prices_all = ut.get_data(syms, dates)  # automatically adds SPY
        # prices = prices_all[syms]  # only portfolio symbols
        # prices_SPY = prices_all["SPY"]  # only SPY, for comparison later
        #
        # '''
        # Indiators
        # '''
        # ind = indicators.Indicators(
        #     symbols="JPM",
        #     start_date=dt.datetime(2008, 1, 1),
        #     end_date=dt.datetime(2009, 12, 31),
        #     period = 14)
        # bbp = ind.bollinger_bands(prices, 14)
        # if self.verbose:
        #     print(bbp)
        #
        #     # example use with new colname
        # volume_all = ut.get_data(
        #     syms, dates, colname="Volume"
        # )  # automatically adds SPY
        # volume = volume_all[syms]  # only portfolio symbols
        # volume_SPY = volume_all["SPY"]  # only SPY, for comparison later
        # if self.verbose:
        #     print(volume)

        pass
            # this method should use the existing policy and test it against new data

    def testPolicy(
            self,
            symbol="IBM",
            sd=dt.datetime(2009, 1, 1, 0, 0),
            ed=dt.datetime(2010, 1, 1, 0, 0),
            sv=100000
    ):
        """
        Tests your learner using data outside of the training data

        :param symbol: The stock symbol that you trained on on
        :type symbol: str
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008
        :type sd: datetime
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009
        :type ed: datetime
        :param sv: The starting value of the portfolio
        :type sv: int
        :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating
            a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.
            Values of +2000 and -2000 for trades are also legal when switching from long to short or short to
            long so long as net holdings are constrained to -1000, 0, and 1000.
        :rtype: pandas.DataFrame
        """

        # here we build a fake set of trades
        # your code should return the same sort of data
        dates = pd.date_range(sd, ed)
        prices_all = ut.get_data([symbol],
                                 dates)  # automatically adds SPY
        prices_SPY = prices_all['SPY']
        prices = prices_all[[symbol,]]

        # print(prices_SPY)
        # print(prices)

        trades = prices_all[[symbol, ]]  # only portfolio symbols
        trades_SPY = prices_all["SPY"]  # only SPY, for comparison later
        trades.values[:, :] = 0  # set them all to nothing

        '''
        indicator funcitons
        '''
        indicators = inds.Indicators(
            symbols=['IBM'],
            start_date=dt.datetime(2009, 1, 1, 0, 0),
            end_date=dt.datetime(2010, 1, 1, 0, 0),
            period = 7,
        )

        # sma = indicators.simple_moving_average(prices.iloc[100:200], 10)
        # print('SMA')
        # print(sma)
        # print('--------------------')
        #
        # b_percent = indicators.bollinger_bands(prices, 10)
        # print('B%')
        # print(b_percent)
        # print('--------------------')
        #
        # so = indicators.stochastic_indicator(prices, 10)
        # print('SO')
        # print(so)
        # print('--------------------')
        #
        # roc = indicators.rate_of_change(prices, 10)
        # print('ROC')
        # print(roc)
        # print('--------------------')
        #
        # macd = indicators.macd_hist(prices)
        # print('MACD')
        # print(macd)
        # print('--------------------')

        # indicators = indicators.Indicators(
        #     symbols = ['IBM'],
        #     sd=dt.datetime(2009, 1, 1, 0, 0),
        #     ed=dt.datetime(2010, 1, 1, 0, 0),
        #     period = 7,
        # )
        # # sma = indicators.Indicators.simple_moving_average(prices, 10)
        # print(sma)


        '''
        Applying indicators to daily to create a rule based algorithm
        '''
        print('here')
        print(prices.shape[0]-1)
        # for i in range(prices.shape[0]-1):
        for i in range(0, 30):
            x = indicators.simple_moving_average(prices[0:i+1], 14)
            print(x)
            # print(prices[0:i+1])
        # if self.verbose:
        #     print(type(trades))  # it better be a DataFrame!
        # if self.verbose:
        #     print(trades)
        # if self.verbose:
        #     print(prices_all)
        return trades

    def author(self):
        return 'tcheng99'


    def study_group(self):
        return 'tcheng99'


if __name__ == "__main__":
    strategy = ManualStrategy(verbose = True)
    strategy.testPolicy()
