__author__ = 'galina'

import Lattice_class
import numpy as np
from random import randint
from random import seed

n = 10
m = 1
D = 1  # can be 1, 1.5 (ladder) or 2

J = 1

Tmin = 0.01
Tmax = 4.0
dT = 0.2

size = n*m

steps_skip = 1000 * size
steps_measure = 5000 * size

def filename(n, m, D):
    if D == 1 and m == 1:
        fname = '1D, ' + str(n) + ' spins'
    elif D == 1.5 and m == 2:
        fname = '1,5D, ' + str(n) + 'x2 spins'
    elif D == 2:
        fname = '2D, ' + str(n) + 'x' + str(m) + ' spins'
    else:
        raise ValueError('Wrong dimensions')
    return fname

temperatures = []
energies = []
magnetizations = []
flips = []

for T in np.arange(Tmin, Tmax, dT):
    lattice = Lattice_class.Lattice(n, m, D, J, T)

    flip = []
    energy = []
    magnetization = []

    for step in range(steps_skip):
        i = randint(0, size - 1)    # spin to flip
        lattice.update(i, lattice.deltaE(i))

    E = lattice.energy()
    M = lattice.magnetization()

    for step in range(steps_measure):
        i = randint(0, size - 1)    # spin to flip
        dE = lattice.deltaE(i)
        dM = lattice.deltaM(i)

        f = lattice.update(i, dE)   # 1 if the spin flips, 0 if stays in the same state

        E += f * dE
        M += f * dM

        energy += [E]
        magnetization += [M]
        flip += [f]

    #     print step, E, lattice.energy(), dE, f, lattice.state
    #
    # print T,
    # print lattice.state
    # print 'E', E, lattice.energy()
    # print 'M', M, lattice.magnetization()


    assert(lattice.energy() == E)
    assert(lattice.magnetization() == M)

    temperatures += [T]
    energies += [np.mean(energy) / size]
    magnetizations += [np.mean(magnetization) / size]
    flips += [flip]

print temperatures
print energies
print magnetizations
