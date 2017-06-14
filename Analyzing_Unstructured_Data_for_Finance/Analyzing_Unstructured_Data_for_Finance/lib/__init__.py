import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sys

import datetime as dt
from datetime import datetime

#from lib.helper_database import 
from lib.helper_system import suppress_warnings
#get rid of missing font warning when plotting:
from matplotlib import rcParams
from matplotlib import style
style.use('ggplot')
from sklearn.externals import joblib



rcParams['font.family'] = 'Droid Sans'

#__all__ makes these names available in Jupyter notebook:
__all__ = ['datetime',
           'dt',
           'joblib',
           'np',
           'pd',
           'plt',
           'rcParams',
           'sns',
           'style',
           'suppress_warnings',
           'sys',
          ] 