from __future__ import division

import Lattice_class
import numpy as np
import pandas as pd
import matplotlib as plt
import os.path
import scipy.integrate
import scipy.stats
import math
from random import randint
from random import seed
import subprocess

def entropy_func(T_list, E_list):
    '''
    returns entropy for given temperature list (T_list) and energy list (E_list) for Ising model.
    Normalized to go to 0 at T = 0
    '''
    beta_list = [1 / x for x in T_list]
    S = []

    for i in range(len(E_list)):
        S += [ E_list[i] * beta_list[i] + scipy.integrate.trapz(E_list[i:], beta_list[i:]) ]

    S = [s - S[-1]  + math.log(2) for s in S]
    S = [s / S[-1] for s in S]

    return S

# 1D and 1.5D: 6, 8, 10, 12, 20, 40
# 2D and 2.5D: 4, 6, 8, 10, (12)

n1 = 12
n2 = 12
n3 = 1
D = 2  # can be 1, 1.5 (ladder), 2 or 2.5 (bilayer)

J = 1

Tmin = 0.2
Tmax = 4.0
dT = 0.1

large_T = range(5, 11) + [15, 20]

T_list = list(np.arange(Tmin, Tmax + dT, dT)) + large_T
T_list = [float(t) for t in T_list]
# T_list = [2.2]

size = n1 * n2 * n3

steps_skip = 5000 * size
steps_measure = 10000 * size

assert((D == 1   and n2 == 1 and n3 == 1) or
       (D == 1.5 and n2 == 2 and n3 == 1) or
       (D == 2   and n3 == 1) or
       (D == 2.5 and n3 == 2))

#fname = str(D) + 'D, ' + str(n1) + 'x' + str(n2) + 'x' + str(n3) + ' spins, T from ' + str(Tmin) + ' to ' + str(Tmax) + '.csv'
#if os.path.exists(fname):
#    raise ValueError('File already exists')

fname = 'no flips, ' + str(D) + 'D, T from ' + str(Tmin) + ' to ' + str(Tmax) + '.csv'

E_list = []
M_list = []
C_list = []
S_list = []
B_list = []
X_list = []

E_se_list = []
M_se_list = []
X_se_list = []

for T in T_list:

    lattice = Lattice_class.Lattice(n1, n2, n3, D, J, T)

    E = []
    M = []
    flip = ''

    for step in range(steps_skip):
        i = randint(0, size - 1)    # spin to flip
        lattice.update(i, lattice.deltaE(i))

    print 'T ' + str(T) + ' termalization done.'

    e = lattice.energy()
    m = lattice.magnetization()

    for step in range(steps_measure):
        i = randint(0, size - 1)    # spin to flip
        de = lattice.deltaE(i)
        dm = lattice.deltaM(i)

        f = lattice.update(i, de)   # 1 if the spin flips, 0 if stays in the same state

        e += f * de
        m += f * dm

        E += [e]
        M += [m]
        flip += str(f)


    assert(lattice.energy() == e)
    assert(lattice.magnetization() == m)


    M2 = list(np.array(M)**2)
    M4 = list(np.array(M)**4)

    energy = np.mean(E) / size
    magnetization = abs(np.mean(M) / size)

    thermal_capacity = (np.var(E) / T**2) / size**2
    binder_cumulant = ( 1 - np.mean(M4) / (3 * np.mean(M2)**2) )
    magnetic_susceptibility = (np.var(M) / T) / size**2

    energy_se = scipy.stats.sem(E) / size
    magnetization_se = np.std(M) / size

    E_list += [energy]
    M_list += [magnetization]
    C_list += [thermal_capacity]
    B_list += [binder_cumulant]
    X_list += [magnetic_susceptibility]

    E_se_list += [energy_se]
    M_se_list += [magnetization_se]

    print 'T ' + str(T) + ' done.'

print 'Writing to file.'

S_list = entropy_func(T_list, E_list)

lattice_type = [str(D) + 'D, ' + str(n1) + 'x' + str(n2) + 'x' + str(n3) + ' spins']*len(T_list)

records = pd.DataFrame({'type'  : lattice_type,
                        'T'     : T_list,
                        'E'     : E_list,
                        'E_se' :  E_se_list,
                        'M'     : M_list,
                        'M_se'  : M_se_list,
                        'C'     : C_list,
                        'S'     : S_list,
                        'B'     : B_list,
                        'X'     : X_list})

# records.to_csv(fname)

if os.path.exists(fname):
    records.to_csv(fname, mode = 'a', header = False)
else:
    records.to_csv(fname)

print fname + ' for ' + str(n1) + 'x' + str(n2) + 'x' + str(n3) + ' spins'

# subprocess.call(['speech-dispatcher'])        #start speech dispatcher
subprocess.call(['spd-say', '"finished"'])