
import pandas as pd
import datetime as dt
import math

import numpy as np

import pandas as pd
from util import get_data, plot_data
import matplotlib.pyplot as plt

from marketsimcode import compute_portvals, assess_portfolio

from TheoreticallyOptimalStrategy import testPolicy, benchmark
# pd.set_option('display.max_row', None)
def build_stocks():
    print('placeholder')

def author():
    """
    :return: The GT username of the student
    :rtype: str
    """
    return "tcheng99"  # Change this to your user ID


def study_group(self):
    return 'tcheng99'



if __name__ == "__main__":




    #Calc TOS
    optimal_trades = testPolicy()

    tos_vals = compute_portvals(optimal_trades, start_val = 100000, commission =0.0, impact = 0.0 )
    # print(tos_vals)
    # cr, adr, sddr, sr, ev, port_val = assess_portfolio(tos_vals, 252,0)
    # # print('TOS vals')
    # # print(cr, adr, sddr, sr, ev, )
    # print(tos_vals)
    normed_tos_vals = tos_vals / tos_vals.iloc[0]
    print(normed_tos_vals)
    # print(normed_tos_vals)
    # print(normed_tos_vals)

    #calc benchmark


    benchmark = benchmark()
    benchmark['Cash'] = 1
    # print(benchmark)
    benchmark_vals = compute_portvals(benchmark, 100000, 0.0, 0.0)
    # cr, adr, sddr, sr, ev, port_val = assess_portfolio(benchmark_vals, 252, 0)
    # print(cr, adr, sddr, sr, ev, )
    # normed_benchmark_vals = benchmark_vals/benchmark_vals.iloc[0]



    # # Prices
    # df = optimal_trades
    # stocks = df.columns[0]

    # prices = get_data([stocks], pd.date_range(df.index[0], df.index[-1]))
    # prices = pd.DataFrame(prices[stocks], columns=[stocks])


    # plt.plot(normed_benchmark_vals, color = "purple" )

    plt.plot(normed_tos_vals, color = "red")
    plt.show()