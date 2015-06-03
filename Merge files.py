from __future__ import division
import os
import pandas as pd

folder = 'temp'

ls = os.listdir(folder)
fname = ls[0][ :-16]
print fname

ls = [folder + '/' + x for x in ls]

data = pd.concat([pd.DataFrame.from_csv(x) for x in ls])
data.sort('T', inplace = True)

data.to_csv(fname + '.csv')