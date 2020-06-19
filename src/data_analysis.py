from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

plt.rcParams['figure.dpi'] = 200


def plot_grid_search(cv_results: Dict, params: List, names: List):
    # Get Test Scores Mean and std for each grid search
    scores_mean = cv_results['mean_test_score']
    scores_mean = np.array(scores_mean).reshape(len(params[0]), len(params[1]))

    scores_sd = cv_results['std_test_score']
    scores_sd = np.array(scores_sd).reshape(len(params[0]), len(params[1]))

    # Plot Grid search scores
    _, ax = plt.subplots(1, 1)

    for idx, val in enumerate(params[0]):
        ax.plot(params[1], scores_mean[idx, :], '-o',
                label=names[0] + ': ' + str(val))

    ax.set_title("Grid Search Scores", fontsize=16, fontweight='bold')
    ax.set_xlabel(names[1], fontsize=12)
    ax.set_ylabel('CV Average Score', fontsize=12)
    ax.legend(loc="best", fontsize=8)
    ax.grid('on')


def test_stationarity(timeseries):
    # adapted from https://www.analyticsvidhya.com/blog/\
    # 2016/02/time-series-forecasting-codes-python/
    # Determing rolling statistics
    plt.rcParams['figure.dpi'] = 150
    plt.rcParams['xtick.labelsize'] = 8

    rolmean = timeseries.rolling(min_periods=1, window="30D").apply(np.nanmean)
    rolstd = timeseries.rolling(min_periods=1, window="30D").apply(np.nanstd)

    # Plot rolling statistics:
    plt.plot(timeseries, color='blue', label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.xlabel("Date")
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

    # Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    ad_test = adfuller(timeseries.dropna(), autolag='AIC')
    df_output = pd.Series(ad_test[0:4],
                          index=['Test Statistic',
                                 'p-value',
                                 '#Lags Used',
                                 'Number of Observations Used'])
    for key, value in ad_test[4].items():
        df_output['Critical Value (%s)' % key] = value
    print(df_output)


def make_stationary(dataframe, time_variable, method):
    plt.rcParams['figure.dpi'] = 100
    # methods are diff or sd
    timeseries = dataframe[time_variable]
    result = adfuller(timeseries.dropna())
    ts_sd = seasonal_decompose(timeseries)
    if (result[0] > result[4]['1%']):
        # Time series is non-stationary
        ts_sd = seasonal_decompose(timeseries)
        init_level = np.min(ts_sd.trend)
        ts_sd.plot()
        ts_diff = timeseries - timeseries.shift(result[2],
                                                fill_value=init_level)
        if (method == 'diff'):
            dataframe['y_stationary'] = ts_diff
        elif (method == 'sd'):
            dataframe['y_stationary'] = ts_sd.resid + ts_sd.seasonal
        result = adfuller(dataframe['y_stationary'].dropna())
    return dataframe, result, ts_sd
