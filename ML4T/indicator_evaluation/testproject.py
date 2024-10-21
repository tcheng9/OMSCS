
import pandas as pd
import datetime as dt
import math

import numpy as np

import pandas as pd
from util import get_data, plot_data
import matplotlib.pyplot as plt
import TheoreticallyOptimalStrategy as tos
from marketsimcode import compute_portvals, assess_portfolio
import indicators

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
    optimal_trades = tos.testPolicy(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000)
    #formatting trades

    '''
    BUILDING OPTIMAL TRADES PORTOFILIO VALUES AND STATS
    '''
    tos_vals = compute_portvals(optimal_trades, start_val = 100000, commission =0.0, impact = 0.0 )
    cr_opt, adr_opt, sddr_opt, sr_opt, ev_opt, port_val_opt = assess_portfolio(tos_vals, 252,0)
    # print(tos_vals)

    normed_tos_vals = tos_vals / tos_vals.iloc[0]
    # print(cr_opt, adr_opt, sddr_opt, sr_opt, ev_opt)


    '''
    BUILDING BENCHMARK PORTFOLIO VALUES AND STATS
    '''

    benchmark = optimal_trades.copy()
    benchmark.iloc[:,:] = 0
    benchmark.iloc[0] = 1000


    benchmark_vals = compute_portvals(benchmark, start_val = 100000, commission =0.0, impact = 0.0)

    cr_bench, adr_bench, sddr_bench, sr_bench, ev_bench, port_val_bench = assess_portfolio(benchmark_vals, 252, 0)

    normed_benchmark_vals = benchmark_vals/benchmark_vals.iloc[0]

    # print(cr_bench, adr_bench, sddr_bench, sr_bench, ev_bench)


    '''
    BUILDING TABLE (DONE VIA A PD DATAFRAME THEN CREATING STATS
    '''
    a = round(cr_bench, 10)

    cr_bench =f'{cr_bench:.6f}'
    adr_bench = f'{adr_bench:.6f}'
    sddr_bench = f'{sddr_bench:.6f}'


    cr_opt = f'{cr_opt:.6f}'
    adr_opt =  f'{adr_opt:.6f}'
    sddr_opt = f'{sddr_opt:.6f}'
    benchmark_list = [cr_bench, adr_bench, sddr_bench]
    opt_list = [cr_opt, adr_opt, sddr_opt]


    # cr_bench.round
    stats_df = pd.DataFrame([benchmark_list, opt_list], columns = ['CR', 'ADR', 'SDDR'], index = ['Benchmark', 'Optimal'])
    stats_df.to_csv('stats.csv', index = True)
    '''
    BUILDING CHART
    '''

    # plt.plot(normed_benchmark_vals, color = "purple" )
    #
    # # plt.xticks(rotation = 45)
    # plt.plot(normed_tos_vals, color = "red")
    # #
    # plt.show()
    # #Statically getting prices
    start_date = dt.datetime(2008, 1, 1)
    sd_before_30 = start_date - dt.timedelta(days=60)
    end_date = dt.datetime(2009, 12, 31)
    symbols = ['JPM']
    # prices = get_data(['JPM'], pd.date_range(sd_before_30, end_date))
    # prices = prices['JPM']
    indicator = indicators.Indicators(symbols, start_date, end_date, 14)
    indicator.build_charts()
    print('here - after buildchart function call')