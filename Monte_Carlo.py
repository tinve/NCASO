__author__ = 'galina'

import Lattice_class
import numpy as np
import pandas as pd
import matplotlib as plt
import os.path
import scipy.integrate
import math
from random import randint
from random import seed

n1 = 4
n2 = 4
n3 = 2
D = 2.5  # can be 1, 1.5 (ladder), 2 or 2.5 (bilayer)

J = 1

Tmin = 1.0
Tmax = 4.0
dT = 0.1

large_T = range(1, 5) + [15, 20]

T_list = list(np.arange(Tmin, Tmax + dT, dT)) + large_T


size = n1 * n2 * n3

steps_skip = 5000 * size
steps_measure = 10000 * size

assert((D == 1   and n2 == 1 and n3 == 1) or
       (D == 1.5 and n2 == 2 and n3 == 1) or
       (D == 2   and n3 == 1) or
       (D == 2.5 and n3 == 2))

# fname_base = str(D) + 'D, ' + str(n1) + 'x' + str(n2) + 'x' + str(n3) + ' spins'

E_list = []
M_list = []
C_list = []
S_list = []
B_list = []
flip_list = []


def entropy(T_list, E_list):
    '''
    returns entropy for given temperature list (T_list) and energy list (E_list) for Ising model.
    Normalized to go to 0 at T = 0
    '''
    beta_list = [1 / T for T in T_list]
    S = []

    for i in xrange(len(E_list)):
        S += [ E_list[i] / T_list[i] + scipy.integrate.trapz(E_list[i:], beta_list[i:]) ]


    S = [s - S[-1]  + math.log(2) for s in S]
    S = [s / S[-1] for s in S]

    return S


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

    # fname = fname_base + ', T = ' + "%0.2f" % T + '.txt'
    #
    # if os.path.exists(fname):
    #     print 'File already exist'
    #
    # f = open(fname, 'w')
    # f.write('T ' + str(temperature) + '\n' +
    #         'E ' + str(energy) + '\n' +
    #         'M ' + str(magnetization) + '\n' +
    #         'C ' + str(thermal_capacity) + '\n' +
    #         'B ' + str(binder_cumulant) + '\n' +
    #         'flips ' + flip)
    #
    # f.close()

    E_list += [energy]
    M_list += [magnetization]
    C_list += [thermal_capacity]
    B_list += [binder_cumulant]
    flip_list += [flip]

    print 'T ' + str(T) + ' done.'

print 'Writing to file.'

S_list = entropy(T_list, E_list)

lattice_type = [str(D) + 'D, ' + str(n1) + 'x' + str(n2) + 'x' + str(n3) + ' spins']*len(T_list)

records = pd.DataFrame({'type'  : lattice_type,
                        'T'     : T_list,
                        'E'     : E_list,
                        'M'     : M_list,
                        'C'     : C_list,
                        'S'     : S_list,
                        'B'     : B_list,
                        'flips' : flip_list})

fname = str(D) + 'D, T from ' + str(Tmin) + ' to ' + str(Tmax) + '.csv'

if not os.path.exists(fname):
#     print 'File already exist'
    records.to_csv(fname)
else:
    records.to_csv(fname, mode = 'a', header = False)
