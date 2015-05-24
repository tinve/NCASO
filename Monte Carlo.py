# Galina Malovichko


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from random import randint, uniform
from scipy import arange

# global parameters

N = 10  # lattice size
J = 1  #

Tmin = 0
Tmax = 4
dT = 0.2

steps_skip = 10000 * N
steps_measure = 4000 * N

# probability model
def prob(dE, T):
    if T == 0:
        if dE > 0:
            return 0
        elif dE < 0:
            return 1
        else:
            return 0.5
    else:
        return 1/(1 + np.exp(dE/T))

# Hamiltonian model (J is global variable here!)
def h(s1, s2):
    return - J * s1 * s2


# Hamiltonian:
def H(lattice):
    H = 0
    for i in range(0, N):
        H = H + h(lattice[i], lattice[(i + 1) % N])
    return H

# single iteration (flipping single spin)
def step(lattice, T):

    lattice_flip = lattice[:]
    i = randint(0, N - 1)
    lattice_flip[i] = - lattice_flip[i]

    dH = H(lattice_flip) - H(lattice)
    p = uniform(0, 1)

    if p <= prob(dH, T):
        lattice = lattice_flip
    return lattice

# average energy of the lattice:
def E(lattice, T, steps_skip, steps_measure):
    e = []

    # skip transient states
    for i in range(0, steps_skip):
        lattice = step(lattice, T)

    for i in range(0, steps_measure):c
        lattice = step(lattice, T)
        e.append(H(lattice))

    return (sum(e)/len(e)) / len(lattice)

# initialize one-dimensional lattice with random spins
lattice = [2 * randint(0, 1) - 1 for i in range(0, N)]

temperatures = []
energies = []

for T in arange(Tmin, Tmax, dT):
    temperatures.append(T)
    energies.append(E(lattice, T, steps_skip, steps_measure))

print temperatures
print energies

plt.plot(temperatures, energies)
plt.show()
