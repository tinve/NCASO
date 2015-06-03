import numpy as np
import pandas as pd
import os
import scipy.integrate
import matplotlib as plt
from pylab import *

def entropy(T_list, E_list):
    '''
    returns entropy for given temperature list (T_list) and energy list (E_list) for Ising model.
    Normalized to go to 0 at T = 0
    '''

#    T_list = T_list.sort()
#    E_list = E_list.sort()
    beta_list = [1 / T for T in T_list]
    S = []

    for i in xrange(len(E_list)):
        S += [ E_list[i] / T_list[i] + scipy.integrate.trapz(E_list[i:], beta_list[i:]) ]


    S = [s - S[-1]  + math.log(2) for s in S]
    S = [s / S[-1] for s in S]

    return S

fname = '1.5D, 20x2x1 spins, T from 1.0 to 4.0.csv'

data = pd.DataFrame.from_csv(fname)

T = list(data['T'])
E = list(data['E'])

S = entropy(T, E)

plt.plot(T, S, 'ko')

data['S'] = S
for t in T:
    print t

data.to_csv(fname)