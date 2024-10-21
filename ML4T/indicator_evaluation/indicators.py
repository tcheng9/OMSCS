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
        self.stochastic_indicator(prices, 14)
        self.rate_of_change(prices, 14)
        self.ema(prices, 10)
        self.macd_line(prices)
        self.signal_line(prices)
        return prices


    def bolinger_bands(self, stocks, period):
        '''
        Setup
        '''
        stock_sd = stocks.copy()
        stock_sd.iloc[0:] = 0


        '''
        Calculating BB upper/lower and percentage
        '''
        rm = stocks.rolling(window = period, min_periods=period).mean()
        std = stocks.rolling(window=period, min_periods=period).std()

        upper_band = rm + (2*std)
        lower_band = rm - (2*std)


        bb_percent = (stocks-lower_band)/(upper_band-lower_band)
        return bb_percent

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


    def stochastic_indicator(self, stocks, period):
        si = stocks.copy()
        si.iloc[0:] = 0
        # period = self.period


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


    def rate_of_change(self, stocks, period):
        roc = stocks.copy()
        roc.iloc[0:] = 0
        # period = 14

        #iterative approach
        for i in range(14, stocks.shape[0]):
            today = stocks.iloc[i]
            past = stocks.iloc[i-period]

            val = ((today-past)/past) * 100

            roc.iloc[i] = val




        return roc

    def ema(self, stocks, period):
        sma = stocks.copy()
        sma.iloc[0:] = 0

        sma = stocks.rolling(window = period, min_periods=period).mean()

        multiplier = (2 /(period+1))

        ema = stocks.copy()
        ema.iloc[0:] = sma

        for i in range(0+period, ema.shape[0]):
            # ema.iloc[i] = stocks.iloc[i] * multiplier + ema.iloc[i-1] * (1-multiplier)
            ema.iloc[i] = (stocks.iloc[i] - ema.iloc[i-1]) * multiplier + ema.iloc[i-1]

        return ema

    def macd_line(self, stocks):
        #calc macd line
        macd = stocks.copy()
        macd.iloc[0:] = 0
        twelve_ema = self.ema(stocks, 12)
        twenty_six_ema = self.ema(stocks, 26)


        macd_line = twelve_ema-twenty_six_ema
        return macd_line

    def signal_line(self, stocks):
        #calc macd line
        macd = stocks.copy()
        macd.iloc[0:] = 0
        twelve_ema = self.ema(stocks, 12)
        twenty_six_ema = self.ema(stocks, 26)


        macd_line = twelve_ema-twenty_six_ema


        nine_ema = self.ema(stocks, 9)

        #calc signal line
        signal = stocks.copy()
        signal.iloc[0:] = 0

        signal = macd_line.rolling(window=9, min_periods=9).mean()

        multiplier = (2 / (9 + 1))
        for i in range(9, macd_line.shape[0]):
            signal.iloc[i] = ((macd_line.iloc[i] - macd_line.iloc[i-1]) * multiplier) + macd_line.iloc[i-1]


        #alternative
        # print(macd_line)
        # signal = self.ema(macd_line[10:], 9)
        # print(signal)

        return signal

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
    sd_before_30 = start_date - dt.timedelta(days=60)
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


    # prices = prices.iloc[20:]
    # normed_prices = prices/prices.iloc[0]
    #
    # plt.plot()
    # plt.plot(normed_prices, color = 'green')
    # plt.plot(normed_sma, color = 'blue')
    #
    # plt.show()

    '''
    Indicator 2 - BB %
    '''
    bbp = indicator.bolinger_bands(prices, 20)
    bbp = bbp[bbp.index > start_date]
    # prices[prices.index > start_date]

    # plt.figure(figsize = (10,8))
    # plt.xticks(rotation = 'vertical')
    # plt.plot(bbp, color = 'pink')
    # plt.show()
    '''
    Indicator 3 - Stochastic Oscillator/Indicator
    '''
    si = indicator.stochastic_indicator(prices, 14)
    # plt.plot(si, color = 'blue')
    # plt.show()

    '''
    Indicator 4 - Rate of Change
    '''
    roc = indicator.rate_of_change(prices, 14)
    # plt.plot(roc, color='green')
    # plt.show()

    '''
    Indicator 5 - MACD
    '''

    # ema = indicator.ema(prices, 20)
    # plt.plot(ema)
    # plt.show()

    # macd = indicator.macd_line(prices)
    # plt.plot(macd, color = 'green')
    # plt.show()
    # signal = indicator.signal_line(prices)
    # plt.plot(signal, color = 'orange')
    # plt.show()

if __name__ == "__main__":
    test_code()
