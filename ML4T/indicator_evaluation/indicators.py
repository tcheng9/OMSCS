
import pandas as pd
import datetime as dt
import math

import numpy as np

import pandas as pd
from util import get_data, plot_data
import matplotlib.pyplot as plt


class Indicators:
    def __init__(self):
        self.stocks = None
        pass

    def get_stocks(self):


        start_date = '2007-12-01'
        end_date = '2009-12-31'

        prices = get_data(['JPM'], pd.date_range(start_date, end_date))
        prices = prices['JPM']
        self.stocks = prices
        #Indicator 1: simple moving average
        self.simple_moving_average(prices)
        self.bolinger_bands(prices)
        self.stochastic_indicator(prices)
        self.rate_of_change(prices)
        self.commodity_channel_index(prices)
        return prices


    def bolinger_bands(self, stocks):
        stock_sd = stocks.copy()
        stock_sd.iloc[0:] = 0
        #BB postive where sma + 2*sd
        bb_pos = stocks.copy()
        bb_pos.iloc[0:] = 0

        ##BB negative where sma - 2 * sd
        bb_neg = stocks.copy()
        bb_neg.iloc[0:] = 0

        # start_row = stocks.iloc[20]
        #getting SD for the entire time period
        period = 14
        for i in range(20, stocks.shape[0]):
            sma = (stocks.iloc[i - period: i + 1].sum(axis=0)) / period
            std = stocks.iloc[i-period:i+1].std()
            bb_pos.iloc[i] = sma + (2 * (std))
            bb_neg.iloc[i] = sma - (2*(std))
        # print('bb pos')
        # print(bb_pos.iloc[20:])
        #
        # print('---------')
        # print('bb neg')
        # print(bb_neg.iloc[20:])

    def simple_moving_average(self, stocks):
        sma = stocks.copy()
        sma.iloc[0:] = 0


        stocks.iloc[10]

        period = 14
        # print(stocks.iloc[20-14:20+1])
        sum_one = stocks.iloc[20-14:20+1].sum(axis =0)
        # print(sum_one)

        for i in range(20, stocks.shape[0]):
            val = (stocks.iloc[i-period: i+1].sum(axis =0)) / period
            sma.iloc[i] = val
        # print(sma.iloc[20:])
        return sma


    def stochastic_indicator(self, stocks):
        si = stocks.copy()
        si.iloc[0:] = 0
        period = 14
        # print(stocks.iloc[20-14:20+1])

        #high over past 14 days
        high = stocks.iloc[20 - 14:20 + 1].max()


        #low of over past 14 days
        low = stocks.iloc[20 - 14:20 + 1].min()

        for i in range(20, stocks.shape[0]):
            high = stocks.iloc[i-period: i+ 1].max()
            low = stocks.iloc[i-period:i+1].min()
            close = stocks.iloc[i]
            val = ((close-low)/(high-low))* 100

            si.iloc[i] = val
        # print(si[20:])



        pass


    def rate_of_change(self, stocks):
        roc = stocks.copy()
        roc.iloc[0:] = 0
        period = 14
        # print(stocks.iloc[20-14:20+1])

        for i in range(20, stocks.shape[0]):
            today = stocks.iloc[i]
            past = stocks.iloc[i-period]

            val = ((today-past)/past) * 100

            roc.iloc[i] = val

        print(roc.iloc[20:])

        pass
    def commodity_channel_index(self, stocks):
        cci = stocks.copy()
        cci.iloc[0:] = 0


        period = 14
        # print(stocks.iloc[20-14:20+1])

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


    indicator = Indicators()
    indicator.get_stocks()
    # indicator.simple_moving_average()
    # indicator.bolinger_bands()



if __name__ == "__main__":
    test_code()
