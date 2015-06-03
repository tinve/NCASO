from __future__ import division
import os
import pandas as pd

folder = '2D, 4x4x1 spins,  4 states library'

ls = os.listdir(folder)
fname = ls[0][ :-16]

ls = [folder + '/' + x for x in ls]

data = pd.concat([pd.DataFrame.from_csv(x) for x in ls])
data.sort('T', inplace = True)

data.to_csv(fname + '.csv')