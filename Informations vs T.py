from __future__ import division

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
from pylab import *

fname = '2D, T from 1.0 to 4.0, processed.csv'

data = pd.DataFrame.from_csv(fname)
# types = data['type'].unique()

T = list(data['T'])
E = list(data['E'])
M = list(data['M'])
C = list(data['C'])
S = list(data['S'])
B = list(data['B'])

hmu = list(data['hmu_average'])
Cmu = list(data['Cmu_average'])
# EE = list(data['EE_average'])

hmu_err_low = list(data['hmu_err_low'])
Cmu_err_low = list(data['Cmu_err_low'])
# EE_err_low = list(data['EE_err_low'])

hmu_err_high = list(data['hmu_err_high'])
Cmu_err_high = list(data['Cmu_err_high'])
# EE_err_high = list(data['EE_err_high'])


plt.plot(T, S, markersize = 6, lw = 3, marker = 'o', alpha = 0.8, label = 'Thermodynamic entropy')
plt.plot(T, hmu, markersize = 3, lw = 1.5, color = 'k', label = 'Entropy rate')



# fname = '1.5D, T from 0.2 to 3.0, processed.csv'
#
# data = pd.DataFrame.from_csv(fname)
# # types = data['type'].unique()
# #
# T = list(data['T'])
# E = list(data['E'])
# M = list(data['M'])
# C = list(data['C'])
# S = list(data['S'])
# B = list(data['B'])
#
# hmu = list(data['hmu_average'])
# Cmu = list(data['Cmu_average'])
# # EE = list(data['EE_average'])
#
# hmu_err_low = list(data['hmu_err_low'])
# Cmu_err_low = list(data['Cmu_err_low'])
# # EE_err_low = list(data['EE_err_low'])
#
# hmu_err_high = list(data['hmu_err_high'])
# Cmu_err_high = list(data['Cmu_err_high'])
# # EE_err_high = list(data['EE_err_high'])
#
#
#
# plt.plot(T, hmu, markersize = 3, lw = 1.5, color = 'k')
# plt.plot(T, S, markersize = 6, lw = 3, alpha = 0.8, marker = 'o', label = '1.5D')
#
# fname = '2D, T from 1.0 to 4.0, processed.csv'
#
# data = pd.DataFrame.from_csv(fname)
# # types = data['type'].unique()
#
# T = list(data['T'])
# E = list(data['E'])
# M = list(data['M'])
# C = list(data['C'])
# S = list(data['S'])
# B = list(data['B'])
#
# hmu = list(data['hmu_average'])
# Cmu = list(data['Cmu_average'])
# # EE = list(data['EE_average'])
#
# hmu_err_low = list(data['hmu_err_low'])
# Cmu_err_low = list(data['Cmu_err_low'])
# # EE_err_low = list(data['EE_err_low'])
#
# hmu_err_high = list(data['hmu_err_high'])
# Cmu_err_high = list(data['Cmu_err_high'])
# # EE_err_high = list(data['EE_err_high'])
#
#
#
# plt.plot(T, hmu, markersize = 3, lw = 1.5, color = 'k')
# plt.plot(T, S, markersize = 6, lw = 3, alpha = 0.8, marker = 'o', label = '2D')
#
#
# fname = '2.5D, T from 1.0 to 4.0, processed.csv'
#
# data = pd.DataFrame.from_csv(fname)
# # types = data['type'].unique()
#
# T = list(data['T'])
# E = list(data['E'])
# M = list(data['M'])
# C = list(data['C'])
# S = list(data['S'])
# B = list(data['B'])
#
# hmu = list(data['hmu_average'])
# Cmu = list(data['Cmu_average'])
# # EE = list(data['EE_average'])
#
# hmu_err_low = list(data['hmu_err_low'])
# Cmu_err_low = list(data['Cmu_err_low'])
# # EE_err_low = list(data['EE_err_low'])
#
# hmu_err_high = list(data['hmu_err_high'])
# Cmu_err_high = list(data['Cmu_err_high'])
# # EE_err_high = list(data['EE_err_high'])
#
#
#
# plt.plot(T, hmu, markersize = 3, lw = 1.5, color = 'k')
# plt.plot(T, S, markersize = 6, lw = 3, alpha = 0.8, marker = 'o', label = '2.5D')



plt.xlim(left = 0, right = 5)
plt.ylim(bottom = -0.05, top = 1.05)

plt.xlabel('$T$', fontsize = 20)
plt.ylabel('Entropy', fontsize = 20, labelpad = 20)

plt.tick_params(axis = 'both', which = 'major', labelsize = 20)

plt.subplots_adjust(left = 0.15, right = 0.92, top = 0.92, bottom = 0.15)
# plt.errorbar(T, EE)
# plt.xlabel('T')
# plt.ylabel('Excess entropy')


# plt.xlim(left = 1.5, right = 3.1)

plt.legend(loc = 4, fontsize = 18)

show()