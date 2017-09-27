import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
from q01_load_data.build import load_data
from q02_data_splitter.build import data_splitter
from q03_linear_regression.build import linear_regression
from q04_linear_predictor.build import linear_predictor
from q05_residuals.build import residuals

import pylab
import scipy.stats as stats


def qq_residuals(error_residuals):
    stats.probplot(error_residuals, dist="norm", plot=pylab)
    return pylab