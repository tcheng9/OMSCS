
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
    print('place other code here')
    optimal_trades = testPolicy()
    tos_vals = compute_portvals(optimal_trades, start_val = 100000, commission =0.0, impact = 0.0 )
    print('here')
    # print(port_vals)

    cr, adr, sddr, sr, ev, port_val = assess_portfolio(tos_vals, 252,0)
    print('TOS vals')
    print(cr, adr, sddr, sr, ev, )


    print('benchmark')

    benchmark = benchmark()
    benchmark_vals = compute_portvals(benchmark, 100000, 0.0, 0.0)
    cr, adr, sddr, sr, ev, port_val = assess_portfolio(benchmark_vals, 252, 0)
    print(cr, adr, sddr, sr, ev, )

    benchmark_vals = benchmark_vals/benchmark_vals[0]
    print(benchmark_vals )
    tos_vals = tos_vals/tos_vals[0]
    plt.plot(benchmark_vals, color = "purple" )
    plt.plot(tos_vals, color = "red")
    plt.show()