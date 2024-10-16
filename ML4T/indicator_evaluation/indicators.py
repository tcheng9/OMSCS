
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
        print('inside of get_stocks')
        of = "./orders/orders-01.csv"
        sv = 1000000
        df = pd.read_csv(of)

        print('\n')
        # start_date = min(df['Date'])
        # end_date = max(df['Date'])

        start_date = '2008-01-01'
        end_date = '2009-12-31'

        stocks = df['Symbol'].unique()
        prices = get_data(['JPM'], pd.date_range(start_date, end_date))
        prices = prices['JPM']
        return prices


    def bolinger_bands(self):
        pass

    def simple_moving_average(self):
        pass

    def stochastic_indicator(self):
        pass

    def commodity_channel_index(self):
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

    of = "./orders/orders-01.csv"
    sv = 1000000
    df = pd.read_csv(of)

    print('\n')
    # start_date = min(df['Date'])
    # end_date = max(df['Date'])

    start_date = '2008-01-01'
    end_date = '2009-12-31'

    stocks = df['Symbol'].unique()
    prices = get_data(['JPM'], pd.date_range(start_date, end_date))
    prices = prices['JPM']



if __name__ == '__main__':

    indicators = Indicators
    prices = indicators.get_stocks()
    print(prices)