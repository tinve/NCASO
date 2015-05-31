__author__ = 'galina'

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
from pylab import *

fname = '2.5D, T from 2.5 to 4.0, processed.csv'

data = pd.DataFrame.from_csv(fname)

hue_order = data['type'].unique()

print data.head()

sns.set_context('paper', font_scale = 1.5, rc = {"lines.linewidth": 1.5})
sns.factorplot('T', 'hmu_average', hue = 'type', hue_order = hue_order, kind = 'point',
               aspect = 1.5, data = data)
savefig(fname[: -4] + ' hmu vs T.png')
#
sns.factorplot('T', 'E_average', hue = 'type', hue_order = hue_order, kind = 'point',
               aspect = 1.5, data = data)
savefig(fname[: -4] + ' Excess Entropy vs T.png')

sns.factorplot('T', 'Cmu_average', hue = 'type', hue_order = hue_order, kind = 'point',
               aspect = 1.5, data = data)
savefig(fname[: -4] + ' Cmu vs T.png')

show()
