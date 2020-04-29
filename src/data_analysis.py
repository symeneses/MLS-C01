import numpy as np

from typing import List, Dict
import matplotlib.pyplot as plt


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
