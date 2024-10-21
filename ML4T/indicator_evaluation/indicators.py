from turtledemo.forest import start

import pandas as pd
import datetime as dt
import math

import numpy as np

import pandas as pd
from util import get_data, plot_data
import matplotlib.pyplot as plt

pd.set_option('display.max_row', None)
class Indicators:
    def __init__(self, symbols,  start_date, end_date, period):

        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date
        self.period = period
        pass

    def get_stocks(self):

        # sd = dt.datetime(2010, 1, 1)
        # sd_before_30 = sd - dt.timedelta(days=30)


        # print(dt.datetime(start_date))

        # #Statically getting prices
        # start_date = dt.datetime(2008, 1, 1)
        # sd_before_30 = start_date - dt.timedelta(days=30)
        # end_date = dt.datetime(2009, 12, 31)
        # prices = get_data(['JPM'], pd.date_range(sd_before_30, end_date))
        # prices = prices['JPM']

        #Dynamically getting prices
        print(self.symbols, self.start_date, self.end_date)
        prices = get_data(self.symbols, pd.date_range(self.start_date, self.end_date) )
        prices = prices['JPM']


        print('\n')
        # # print(prices[prices.index[start_date, end_date]])
        # print(prices)
        # print(prices[prices.index > start_date])
        # sd = dt.datetime(2010, 1, 1), ed = dt.datetime(2011, 12, 31), sv = 100000):


        self.stocks = prices
        # #Indicator 1: simple moving average
        self.simple_moving_average(prices, 14)
        self.bolinger_bands(prices, 14)
        self.stochastic_indicator(prices)
        self.rate_of_change(prices)
        self.commodity_channel_index(prices)
        return prices


    def bolinger_bands(self, stocks, period):
        '''
        Setup
        '''
        stock_sd = stocks.copy()
        stock_sd.iloc[0:] = 0
        #BB postive where sma + 2*sd
        bb_pos = stocks.copy()
        bb_pos.iloc[0:] = 0

        ##BB negative where sma - 2 * sd
        bb_neg = stocks.copy()
        bb_neg.iloc[0:] = 0

        bbp = stocks.copy()
        bbp.iloc[0:] = 0

        '''
        Calculating BB upper/lower and percentage
        '''


        #getting SD for the entire time period

        # for i in range(20, stocks.shape[0]-1):
        #     sma = (stocks.iloc[i - period: i + 1].sum(axis=0)) / period
        #     std = stocks.iloc[i-period:i+1].std()
        #     bb_pos.iloc[i] = sma + (2 * (std))
        #     bb_neg.iloc[i] = sma - (2*(std))
        sma = self.simple_moving_average(stocks, 14)
        #vectorized approach
        # bbp.iloc[i] = ((((price.iloc[i-period+1:i+1])) - sma[i]) ** 2).sum()
        # print(sma.shape)
        # print(stocks.shape)
        for i in range(20, stocks.shape[0]):
            # # print(stocks.iloc[i-period+1:i])

            bbp.iloc[i] = ((stocks.iloc[i-period+1:i] - sma.iloc[i]) ** 2).sum()
        #     stocks.iloc[i-period+1:i+1]
        # print(bbp)
        # print(sma[0])
        # print(bbp)
        return bbp
    def simple_moving_average(self, stocks, period):

        sma = stocks.copy()
        sma.iloc[0:] = 0


        # stocks.iloc[10]

        period = 14


        # print(stocks)
        # #iterative approach -> NOTE: I'M PRETTY SURE THE MATH IS OFF HERE SO CORRECT IF I USE BUT DOUBT I WILL USE
        # for i in range(0, stocks.shape[0]):
        #     val = (stocks.iloc[i-period: i+1].sum(axis =0)) / period
        #     sma.iloc[i] = val
        # # print(sma.iloc[20:])
        # # print(sma)
        #
        # print('-----------------')
        #vecotrized approach

        sma = stocks.rolling(window = period, min_periods = period).mean()
        # print(sma)
        # sma = sma.iloc[20:]

        return sma


    def stochastic_indicator(self, stocks):
        si = stocks.copy()
        si.iloc[0:] = 0
        period = self.period


        # #high over past 14 days
        # high = stocks.iloc[20 - 14:20 + 1].max()
        #
        #
        # #low of over past 14 days
        # low = stocks.iloc[20 - 14:20 + 1].min()
        #
        #iterative approach
        # for i in range(20, stocks.shape[0]):
        #     high = stocks.iloc[i-period: i+ 1].max()
        #     low = stocks.iloc[i-period:i+1].min()
        #     close = stocks.iloc[i]
        #     val = ((close-low)/(high-low))* 100
        #
        #     si.iloc[i] = val

        #vectorized approach
        high_over_period = stocks.rolling(window = period, min_periods = period).max()
        low_over_period = stocks.rolling(window=period, min_periods=period).min()
        # print(min_over_period.iloc[20:30], high_over_period.iloc[20:30])

        si = ((stocks-low_over_period) / (high_over_period-low_over_period) ) * 100
        # print(si)
        return si


    def rate_of_change(self, stocks):
        roc = stocks.copy()
        roc.iloc[0:] = 0
        period = 14


        for i in range(20, stocks.shape[0]):
            today = stocks.iloc[i]
            past = stocks.iloc[i-period]

            val = ((today-past)/past) * 100

            roc.iloc[i] = val



        pass
    def commodity_channel_index(self, stocks):
        cci = stocks.copy()
        cci.iloc[0:,] = 0


        period = 14


        # high over past 14 days
        high = stocks.iloc[20 - 14:20 + 1].max()

        # low of over past 14 days
        low = stocks.iloc[20 - 14:20 + 1].min()

        #creating typical price
        tp = stocks.copy()
        tp.iloc[0:] = 0
        for i in range(20, stocks.shape[0]):
            high = stocks.iloc[i - period: i + 1].max()
            low = stocks.iloc[i - period:i + 1].min()
            close = stocks.iloc[i]
            tp.iloc[i] = (high + low + close) / 3

        #creating moving average OF TYPICAL PRICE OVER P PERIODS
        ma_tp = stocks.copy()
        ma_tp.iloc[0:] = 0


        for i in range(20, stocks.shape[0]):
            val = (tp.iloc[i-period: i+1].sum(axis =0)) / period
            ma_tp[i] = val

        #calculating mean deviation
        md = stocks.copy()
        md.iloc[0:] = 0


        for i in range(20, stocks.shape[0]):
            diff = tp[i-period:i+1] - ma_tp[i-period: i+1]
            abs_diff = diff.abs()
            sum_abs_diff = abs_diff.sum()
            md[i] = sum_abs_diff/period

        for i in range(20, stocks.shape[0]):
            cci[i] = (tp.iloc[i] - ma_tp.iloc[i]) / (0.015 * md.iloc[i])


        pass


def author():
    """
    :return: The GT username of the student
    :rtype: str
    """
    return "tcheng99"  # Change this to your user ID


def study_group(self):
    return 'tcheng99'

def test_code():
    """
    Helper function to test code
    """
    # this is a helper function you can use to test your code
    # note that during autograding his function will not be called.
    # Define input parameters

    # #Statically getting prices
    start_date = dt.datetime(2008, 1, 1)
    sd_before_30 = start_date - dt.timedelta(days=30)
    end_date = dt.datetime(2009, 12, 31)
    symbols = ['JPM']
    # prices = get_data(['JPM'], pd.date_range(sd_before_30, end_date))
    # prices = prices['JPM']
    indicator = Indicators(symbols, sd_before_30, end_date, 14)
    prices = indicator.get_stocks()

    '''
    Indicator 1 - SMA
    '''
    sma = indicator.simple_moving_average(prices, 14)
    sma = sma.iloc[20:]
    normed_sma = sma/sma.iloc[0]
    # print(normed_sma)


    prices = prices.iloc[20:]
    normed_prices = prices/prices.iloc[0]
    #
    # plt.plot()
    # plt.plot(normed_prices, color = 'green')
    # plt.plot(normed_sma, color = 'blue')
    #
    # plt.show()

    '''
    Indicator 2 - BB %
    '''
    # bbp = indicator.bolinger_bands(prices, 14)
    # # print(bbp)
    # normed_bbp = bbp/bbp.iloc[20]
    # print(bbp.iloc[20])
    # print(normed_bbp)
    # # plt.plot()
    # plt.plot(normed_bbp.iloc[20:], color = 'purple')
    # # plt.plot(normed_sma, color = 'blue')
    # #
    # plt.show()

    '''
    Indicator 3 - Stochastic Oscillator/Indicator
    '''
    si = indicator.stochastic_indicator(prices)
    plt.plot(si, color = 'blue')
    plt.show()
if __name__ == "__main__":
    test_code()
