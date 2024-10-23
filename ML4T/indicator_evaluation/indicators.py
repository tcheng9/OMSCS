from turtledemo.forest import start

import pandas as pd
import datetime as dt
import math

import numpy as np

import pandas as pd
from util import get_data, plot_data
import matplotlib.pyplot as plt

# pd.set_option('display.max_row', None)
class Indicators:
    def __init__(self, symbols,  start_date, end_date, period):

        self.symbols = symbols
        self.start_date = start_date
        self.sd_before_period = start_date - dt.timedelta(days = 60)
        self.end_date = end_date
        self.period = period
        self.stocks = None
        pass


    def build_charts(self):

        '''
        Control date here
        '''
        sd_before_period = self.start_date - dt.timedelta(days = 60)

        # Dynamically getting prices
        prices = get_data(self.symbols, pd.date_range(sd_before_period, self.end_date))
        prices = prices['JPM']
        self.stocks = prices



        '''
        Build DF and Chart for indicator 1: SMA
        '''
        sma = self.simple_moving_average(prices, 14)

        #Building chart
        sma = sma[sma.index > self.start_date]
        normed_sma = sma / sma.iloc[0]

        prices_correct_sd = prices[prices.index > self.start_date]
        normed_prices = prices_correct_sd/prices_correct_sd.iloc[0]

        plt.figure(figsize=(10, 8))
        plt.plot(normed_prices, color='orange', label = 'prices')
        plt.plot(normed_sma, color='blue', label = 'SMA')
        plt.legend()
        plt.ylabel('Price')
        plt.xlabel('Date')
        plt.title('Simple Moving Average')
        # plt.figure(figsize=(10, 8))
        plt.xticks(rotation='40')

        plt.savefig('sma.png')
        plt.close()
        print('SMA chart built')
        '''
        Build DF and Chart for indicator 2: Bolinger Band Percentage
        '''

        bbp = self.bolinger_bands(prices, 14)
        bbp = bbp[bbp.index > self.start_date]

        # prices[prices.index > start_date]

        plt.figure(figsize=(10, 8))
        plt.xticks(rotation=40)
        plt.plot(bbp, color='green', label = 'BB%')
        plt.title('Bolinger Bands Percentage')
        plt.xlabel('Date')
        plt.ylabel('Perecentage')
        plt.legend()
        # plt.show()
        plt.savefig('./graphs/bbpercent.png')
        plt.close()
        print('bb% built')
        '''
        Build DF and Chart for indicator 3: Stochastic indicator/oscillator
        '''

        si = self.stochastic_indicator(prices, 14)
        si = si[si.index>self.start_date]

        plt.figure(figsize=(10, 8))
        plt.xticks(rotation=40)
        plt.plot(si, color='orange', label='Stochastic Oscillator')
        plt.title('Stochastic Oscillator')
        plt.xlabel('Date')
        plt.ylabel('%K')
        plt.legend()
        # plt.show()
        plt.savefig('./graphs/so.png')
        plt.close()
        print('stochastic indicator built')
        '''
        Build DF and Chart for indicator 4: Rate of Change
        '''
        roc = self.rate_of_change(prices, 14)
        roc = roc[roc.index > self.start_date]
        plt.figure(figsize=(10, 8))
        plt.xticks(rotation=40)
        plt.plot(roc, color='red', label='Rate of Change')
        plt.title('Rate of Change')
        plt.xlabel('Date')
        plt.ylabel('Rate of Change')
        plt.legend()
        # plt.show()
        plt.savefig('./graphs/roc.png')
        plt.close()
        # plt.plot(roc, color='green')
        # plt.savefig('./graphs/roc.png')
        '''
        Build DF and Chart for indicator 5: MACD
        (includes MACD line, signal line and MACD histogram)
        '''
        # self.ema(prices, 10)
        '''
        Indicator 5 : MACD
        '''
        plt.figure(figsize=(10, 8))
        macd_line = self.macd_line(prices)
        plt.plot(macd_line, color='green', label = 'MACD line')


        signal_line = self.signal_line(prices)
        plt.plot(signal_line, color='orange', label = 'Signal line')

        macd_hist = self.macd_hist(prices)
        plt.bar(x=macd_hist.index, height=macd_hist, label = 'MACD histogram')

        plt.ylabel('MACD')
        plt.xlabel('Date')
        plt.title('MACD Lines')

        plt.xticks(rotation=40)
        plt.show()


        # return prices


    def get_stocks(self):

        sd_before_30 = self.start_date - dt.timedelta(days=60)
        #Dynamically getting prices
        prices = get_data(self.symbols, pd.date_range(sd_before_30, self.end_date) )
        prices = prices['JPM']


        self.stocks = prices

        '''
        Build DF and Chart for indicator 1: SMA
        '''
        sma = self.simple_moving_average(prices, 14)


        '''
        Build DF and Chart for indicator 2: Bolinger Band Percentage
        '''
        # self.bolinger_bands(prices, 14)
        '''
        Build DF and Chart for indicator 3: Stochastic indicator/oscillator
        '''

        # self.stochastic_indicator(prices, 14)

        '''
        Build DF and Chart for indicator 4: Rate of Change
        '''
        # self.rate_of_change(prices, 14)
        '''
        Build DF and Chart for indicator 5: MACD
        (includes MACD line, signal line and MACD histogram)
        '''
        # self.ema(prices, 10)
        '''
        Indicator 1 - SMA
        '''
        # self.macd_line(prices)
        # self.signal_line(prices)
        # self.macd_hist(prices)
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
        sma = stocks.rolling(window = period, min_periods = period).mean()


        return sma


    def stochastic_indicator(self, stocks, period):
        #AKA stochastic oscillator
        si = stocks.copy()
        si.iloc[0:] = 0

        #vectorized approach
        high_over_period = stocks.rolling(window = period, min_periods = period).max()
        low_over_period = stocks.rolling(window=period, min_periods=period).min()


        si = ((stocks-low_over_period) / (high_over_period-low_over_period) ) * 100

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
        # calc signal line
        ##Using 9 day period
        period = 9
        signal = stocks.copy()
        signal.iloc[0:] = 0

        ret_signal = stocks.copy()
        ret_signal.iloc[0:] = 0
        macd_line = self.macd_line(stocks)



        sma_macd_line = macd_line.rolling(window = period, min_periods=period).mean()

        signal = sma_macd_line
        multiplier = (2 / (period + 1))

        for i in range(period, sma_macd_line.shape[0]):
            ret_signal.iloc[i] = ((macd_line.iloc[i] - signal.iloc[i-1])*multiplier)+signal.iloc[i-1]

        return ret_signal

    def macd_hist(self, stocks):
        macd_line = self.macd_line(stocks)
        signal_line = self.signal_line(stocks)
        macd_hist = macd_line - signal_line

        return macd_hist




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
    print('you are running test_code')
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


    prices = prices.iloc[20:]
    normed_prices = prices/prices.iloc[0]
    #
    plt.plot()
    plt.plot(normed_prices, color = 'green')
    plt.plot(normed_sma, color = 'blue')

    plt.savefig('./graphs/sma.png')

    '''
    Indicator 2 - BB %
    '''
    bbp = indicator.bolinger_bands(prices, 20)
    bbp = bbp[bbp.index > start_date]
    # prices[prices.index > start_date]

    plt.figure(figsize = (10,8))
    plt.xticks(rotation = 'vertical')
    plt.plot(bbp, color = 'pink')
    plt.savefig('./graphs/bbpercent.png')
    '''
    Indicator 3 - Stochastic Oscillator/Indicator
    '''
    si = indicator.stochastic_indicator(prices, 14)
    plt.plot(si, color = 'blue')
    plt.savefig('./graphs/si.png')

    '''
    Indicator 4 - Rate of Change
    '''
    roc = indicator.rate_of_change(prices, 14)
    plt.plot(roc, color='green')
    plt.savefig('./graphs/roc.png')

    '''
    Indicator 5 - MACD
    '''

    ema = indicator.ema(prices, 20)
    plt.plot(ema)
    plt.savefig('./graphs/ema.png')
    '''
    5.1 - MACD LINE
    '''
    macd = indicator.macd_line(prices)
    plt.plot(macd, color = 'green')
    plt.savefig('./graphs/macd_line.png')

    '''
    5.2 - MACD - SIGNAL Line
    '''
    signal = indicator.signal_line(prices)
    plt.plot(signal, color = 'orange')
    plt.savefig('./graphs/macd_signal.png')

    '''
    5.3 - MACD - Histogram
    '''
    macd_hist = indicator.macd_hist(prices)
    plt.bar(x= macd_hist.index, height = macd_hist)
    plt.savefig('./graphs/macd_hist.png')
if __name__ == "__main__":
    # test_code()
    print('nothing should happen')