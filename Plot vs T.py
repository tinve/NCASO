__author__ = 'galina'

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
from pylab import *

fname = '2.5D, T from 2.5 to 4.0.csv'

data = pd.DataFrame.from_csv(fname)

hue_order = data['type'].unique()

sns.set_context('paper', font_scale = 1.5, rc = {"lines.linewidth": 1.5})
sns.factorplot('T', 'E', hue = 'type', hue_order = hue_order, kind = 'point',
               aspect = 1.5, data = data)
savefig(fname[: -4] + ' E vs T.png')

sns.factorplot('T', 'M', hue = 'type', hue_order = hue_order, kind = 'point',
               aspect = 1.5, data = data)
savefig(fname[: -4] + ' M vs T.png')

sns.factorplot('T', 'C', hue = 'type', hue_order = hue_order, kind = 'point',
               aspect = 1.5, data = data)
savefig(fname[: -4] + ' C vs T.png')

sns.factorplot('T', 'B', hue = 'type', hue_order = hue_order, kind = 'point',
               aspect = 1.5, data = data)
savefig(fname[: -4] + ' B vs T.png')
show()

