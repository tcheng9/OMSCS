
import pandas as pd
import datetime as dt
import math

import numpy as np

import pandas as pd
from util import get_data, plot_data
import matplotlib.pyplot as plt
from marketsimcode import compute_portvals, assess_portfolio
from TheoreticallyOptimalStrategy import testPolicy
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
    trades = testPolicy()
    port_vals = compute_portvals(trades, start_val = 1000000, commission =0.0, impact = 0.0 )
    print('here')
    print(port_vals)
    cr, adr, sddr, sr, ev, port_val = assess_portfolio(port_vals, 0,0)
    print(cr, adr, sddr, sr, ev, )
