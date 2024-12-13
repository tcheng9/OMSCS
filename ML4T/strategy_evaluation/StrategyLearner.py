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
import RTLearner as rtl
import DTLearner as dtl
import BagLearner as bagl
import pandas as pd
import util as ut
import indicators as inds
import numpy as np
pd.set_option('display.max_rows', 500)
class StrategyLearner(object):
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
        self.model = None


    # this method should create a QLearner, and train it for trading
    def add_evidence(
        self,
        symbol="IBM",
        sd=dt.datetime(2008, 1, 1),
        ed=dt.datetime(2009, 1, 1),
        sv=10000,
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

        # example usage of the old backward compatible util function
        syms = [symbol]
        dates = pd.date_range(sd, ed)
        prices_all = ut.get_data(syms, dates)  # automatically adds SPY
        prices = prices_all[syms]  # only portfolio symbols
        prices_SPY = prices_all["SPY"]  # only SPY, for comparison later
        if self.verbose:
            print(prices)

        # example use with new colname
        volume_all = ut.get_data(
            syms, dates, colname="Volume"
        )  # automatically adds SPY
        volume = volume_all[syms]  # only portfolio symbols
        volume_SPY = volume_all["SPY"]  # only SPY, for comparison later
        if self.verbose:
            print(volume)

        '''''''''''''''''''''''''''''''''''
        #####################################
        MY CODE STARTS HERE
        #####################################
        '''''''''''''''''''''''''''''''''''




        '''
        Building dataset
        '''
        # print(prices)
        data = prices.copy()
        data['SMA'] = 0
        data['B%'] = 0
        data['SO'] = 0
        data['ROC'] = 0
        data['MACD'] = 0
        # print(data)

        x_len = data.shape[0] - 1

        #
        x_len_seventy = int(x_len*.7)
        x_len_thirty = int(x_len*.3)
        print(data.shape)
        # print(data[175)])


        indicators = inds.Indicators(
            symbols=['IBM'],
            start_date=dt.datetime(2009, 1, 1, 0, 0),
            end_date=dt.datetime(2010, 1, 1, 0, 0),
            period=7,
        )
        '''
        Calculating the specific indicator for a provided set of stock prices
        '''
        '''
        Building X_vector
        '''
        sma = indicators.simple_moving_average(prices, 14)
        b_percent = indicators.bollinger_bands(prices, 14)
        so = indicators.stochastic_indicator(prices, 14)
        roc = indicators.rate_of_change(prices, 14)
        macd = indicators.macd_hist(prices)


        # print(data.columns)
        data = data.drop(data.columns[0], axis = 1)

        data['SMA'] = sma
        data['B%'] = b_percent
        data['SO'] = so
        data['ROC'] = roc
        data['MACD'] = macd

        '''
        Building y_vector
        '''
        n = 5
        #vectorized approach somehow
        # ret = (prices[t+n] / prices[t]) - 1.0

        ret = prices.copy()
        ret.iloc[:, 0] = 0
        ret = ret[ret.columns[0]]
        y = pd.array([0] * (prices.shape[0]-1))
        # print(ret)
        for i in range(ret.shape[0]-n):
            ret.iloc[i] = (prices.iloc[i+n] / prices.iloc[i]) - 1.0
        # print(ret)
        ybuy = .01
        ysell = -.01
        for i in range(ret.shape[0]-n):
            # print(i)
            if ret.iloc[i] > ybuy:
                y[i] = 1
            elif ret.iloc[i] < ysell:
                y[i] = -1
            else:
                y[i] = 0


        '''
        Spltting data into train/test
        
        Question: do I need to randomly resample for bagger?
        Question: wouldn't this cause issues with linear time constraint? don't train future to predict past?
        '''
        # #split data once dataset is created
        x_train = data.iloc[:x_len_seventy, :]
        x_test = data.iloc[x_len_seventy:, :]
        # #
        y_train = y[:x_len_seventy]
        y_test = y[x_len_thirty:]

        # print(x_train.mean())
        x_train = x_train.fillna(x_train.mean())
        x_test = x_test.fillna(x_test.mean())
        print(x_train.shape)
        print(y_train.shape)
        '''
        Implementing ML model 
        '''
        model = bagl.BagLearner(
            learner=rtl.RTLearner,
            kwargs={'leaf_size': 5},
            bags=20,
            boost=False,
            verbose=False
        )
        # # model = dtl.DTLearner(leaf_size = 5)
        # model = rtl.RTLearner(leaf_size=5)
        # print('x train is')
        # print(x_train)
        # print('------------')
        # #
        # print('y train is')
        # print(y_train)
        # print('------------')


        # x_train = x_train[['SMA', 'B%']]

        # print(x_train.iloc[0:10])
        # print(y_train[0:10])
        #
        # x_train = x_train.iloc[0:1]
        # y_train = y_train[0:1]
        # print('shpes are')
        # print(x_train.shape)
        # print(y_train.shape)
        # print(y_train[0:20])
        # print('before model call')
        # x_train = np.array([
        #     [110.120188, 0.559117],
        #     [110.120188, 0.559117],
        #     [110.120188, 0.559117],
        #     [92.910000, 0.505818],
        #     [93.002857, 0.978122],
        #     [93.134286, 0.992156],
        #     [93.357143, 0.746369],
        #     [93.680714, 0.747927],
        #     [94.239286, 0.801220],
        #     [94.720714, 0.730926],
        #     [110.120188, 0.559117],
        #     [110.120188, 0.559117],
        #     [110.120188, 0.559117],
        #     [92.910000, 0.505818],
        #     [93.002857, 0.978122],
        #     [93.134286, 0.992156],
        #     [93.357143, 0.746369],
        #     [93.680714, 0.747927],
        #     [94.239286, 0.801220],
        #     [94.720714, 0.730926],
        # ])
        # y_train = np.array([-1, -1, -1, 1, 0, 1, 1, 1, 0, 1, -1, -1, -1, 1, 0, 1, 1, 1, 0, 1])
        # x_train = x_train.iloc[0:100]
        # y_train = y_train[0:100]
        # print(x_train.shape)
        # print(y_train.shape)
        # print(x_train.to_numpy())
        x_train = x_train.to_numpy()
        model.add_evidence(x_train,y_train)

        res = model.query(x_test.to_numpy())
        print(res)

    # this method should use the existing policy and test it against new data
    def testPolicy(
        self,
        symbol="IBM",
        sd=dt.datetime(2009, 1, 1),
        ed=dt.datetime(2010, 1, 1),
        sv=10000,
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
        prices_all = ut.get_data([symbol], dates)  # automatically adds SPY
        trades = prices_all[[symbol,]]  # only portfolio symbols
        trades_SPY = prices_all["SPY"]  # only SPY, for comparison later
        trades.values[:, :] = 0  # set them all to nothing
        trades.values[0, :] = 1000  # add a BUY at the start
        trades.values[40, :] = -1000  # add a SELL
        trades.values[41, :] = 1000  # add a BUY
        trades.values[60, :] = -2000  # go short from long
        trades.values[61, :] = 2000  # go long from short
        trades.values[-1, :] = -1000  # exit on the last day
        if self.verbose:
            print(type(trades))  # it better be a DataFrame!
        if self.verbose:
            print(trades)
        if self.verbose:
            print(prices_all)
        return trades

    def study_group(self):
        return 'tcheng99'


if __name__ == "__main__":
    print("One does not simply think up a strategy")
    learner = StrategyLearner()
    learner.add_evidence(
        symbol="IBM",
        sd=dt.datetime(2008, 1, 1),
        ed=dt.datetime(2009, 1, 1),
        sv=10000,
    )