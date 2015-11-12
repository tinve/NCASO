from __future__ import division

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
from pylab import *

fname = 'no flips, 2D, T from 0.2 to 4.0.csv'
to_plot = 'E'

data = pd.DataFrame.from_csv(fname)
types = data['type'].unique()

for i in range(len(types)):
    print i, types[i]

# types = [types[18]] + [types[14]] + [types[9]] + [types[12]]

for i in range(len(types)):
    print i, types[i]

# sns.set_context('poster')

for i, type in enumerate(types[1:]):

    data_subset = data[data['type'] == type]
    T = list(data_subset['T'])

    Y = list(data_subset[to_plot])
    Y_err = [0] * len(Y)

#    Y_err = list(data_subset[to_plot + '_std'])
#    plt.errorbar(T[:], Y[:], yerr = Y_err, markersize = 5, marker = 'o', label = type)

    plt.plot(T[3:], Y[3:], markersize = 5, lw = 3, marker = 'o', label = type[4:-8] + ' spins')

    # if i == 0:
    #      plt.plot(T[:], Y[:], markersize = 5, lw = 3, marker = 'o', label = '1D')
    # elif i == 1 :
    #      plt.plot(T[1:], Y[1:], markersize = 5, lw = 3, marker = 'o', label = '1.5D')
    # elif i == 2 :
    #      plt.plot(T[1:], Y[1:], markersize = 5, lw = 3, marker = 'o', label = '2D')
    # else:
    #      plot(T[7:], Y[7:], markersize = 5, lw = 3, marker = 'o', label = '2.5D')

plt.xlabel('$T$', fontsize = 20)
plt.ylabel('$E$', fontsize = 20, rotation = 'horizontal', labelpad = 25)

#plt.axvline(x = 2.2, lw = 5, color = 'k', alpha = 0.2)

plt.subplots_adjust(left = 0.15, right = 0.92, top = 0.92, bottom = 0.15)
plt.tick_params(axis = 'both', which = 'major', labelsize = 20)


plt.xlim(left = 0, right = 5)
plt.ylim(bottom = -2.1, top = 0)
legend = plt.legend(fontsize = 18, loc = 2)
show()