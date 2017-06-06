import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import seaborn as sns
import sys

from datetime import datetime

#get rid of missing font warning when plotting:
from matplotlib import rcParams

from matplotlib import style
style.use('ggplot')

#from lib.helper_database import 
from lib.helper_system import suppress_warnings

rcParams['font.family'] = 'Droid Sans'

#__all__ makes these names available in Jupyter notebook:
__all__ = ['datetime',
           'np',
           'pd',
           'pdr',
           'plt',
           'rcParams',
           'sns',
           'sys',
           'suppress_warnings',
          ] 