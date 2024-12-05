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

        '''
        Calculating the specific indicator for a provided set of stock prices
        '''
        sma = indicators.simple_moving_average(prices, 14)
        b_percent = indicators.bollinger_bands(prices, 14)
        so = indicators.stochastic_indicator(prices, 14)
        roc = indicators.rate_of_change(prices, 14)
        macd = indicators.macd_hist(prices)

        '''
        Getting buy/out/sell signal from a single indicator
        '''
        # sma_signal = self.sma_pred(sma)


        '''
        Applying indicators to daily to create a rule based algorithm
        '''
        # print('here')
        # print(prices.shape[0]-1)
        # for i in range(prices.shape[0]-1):
        for i in range(1, 50):
            '''
            SMA signal prediction
            '''

            sma = indicators.simple_moving_average(prices[0:i+1], 14)
            sma_signal = self.sma_pred(sma)


            '''
            B% signal
            '''
            b_percent = indicators.bollinger_bands(prices[0:i+1], 14)
            b_signal = self.b_pred(b_percent)
            '''
            SO signal
            '''

            so = indicators.stochastic_indicator(prices[0:i+1], 14)
            so_signal = self.so_pred(so)
            '''
            ROC signal
            '''

            roc = indicators.rate_of_change(prices[0:i+1], 14)
            roc_signal = self.roc_pred(roc)
            '''
            MACD signal
            '''
            macd = indicators.macd_hist(prices[0:i+1])
            macd_signal = self.macd_pred(macd)


            print(sma_signal, '|', b_signal, '|', so_signal, '|', roc_signal, '|', macd_signal)
            print('--------')

            # print(x)
            # print(prices[0:i+1])
        # if self.verbose:
        #     print(type(trades))  # it better be a DataFrame!
        # if self.verbose:
        #     print(trades)
        # if self.verbose:
        #     print(prices_all)
        return trades

    '''
    Indicator signals:
        -1 : short
        0 : out (?) / do nothing
        1 : buy long
    '''

    def sma_pred(self, metric):
        # print(metric)
        if metric.iloc[-1, 0] < metric.iloc[-2, 0]:
            #if today's price < yesterday's price -> decreasing
            #if DECREASING -> short
            return -1
        elif metric.iloc[-1, 0] > metric.iloc[-2, 0]:
            # if today's price < yesterday's price -> decreasing
            return 1
        else:

            '''
            QUESTION: DO I GO BACK TO 0 OR JUST HOLD?
            '''
            # print('stayed the same')
            return 0

        # pass
    def b_pred(self, metric):
        # print(metric)
        #you only have to look at today's B%. If the increase is
        if metric.iloc[-1, 0] > .8:
            #buy since > .8
            return 1
        elif metric.iloc[-1, 0] < .2:
            #sell signal since < .2
            return -1
        else:
            #exit/do nothing since signal is between .2 < signal < .8
            return 0

    def roc_pred(self, metric):
        # print(metric)
        if metric.iloc[-1, 0] < 0:
            #price is decreasing at a certain rate THEREFORE short
            return -1
        elif metric.iloc[-1, 0] > 0:
            #price is increasing at a certain rate -> buy long
            return 1
        else:
            #price is exactly the same -> do nothing
            return 0

    def so_pred(self, metric):
        # print(metric)
        if metric.iloc[-1, 0] < 20:
            return -1
        elif metric.iloc[-1, 0] > 80:
            return 1
        else:
            return 0

    def macd_pred(self, metric):
        # print(metric)
        if metric.iloc[-1, 0] < 0:
            # price is decreasing at a certain rate THEREFORE short
            return -1
        elif metric.iloc[-1, 0] > 0:
            # price is increasing at a certain rate -> buy long
            return 1
        else:
            # price is exactly the same -> do nothing
            return 0


    def author(self):
        return 'tcheng99'

    def study_group(self):
        return 'tcheng99'


if __name__ == "__main__":
    strategy = ManualStrategy(verbose = True)
    strategy.testPolicy()
