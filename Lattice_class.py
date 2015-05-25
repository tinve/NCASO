from __future__ import division
import math
from random import randint
from random import uniform

class Lattice:
    def __init__(self, n, m, D, J, T):

        self.size = n * m
        self.state = [2 * randint(0, 1) - 1 for i in range(n * m)]

        self.n = n
        self.m = m
        self.D = D
        self.J = J
        self.T = T

        if D == 1 and m == 1:
            self.neighbor = {}

            for i in range(n):
                self.neighbor[i] = [(i - 1) % n,
                                    (i + 1) % n]

        if D == 1.5 and m == 2:
            self.neighbor = {}

            for i in range(n):
                self.neighbor[i] = [(i - 1) % n,
                                    (i + 1) % n,
                                    (i + n) % (2 * n)]
            for i in range(n, 2 * n):
                self.neighbor[i] = [(i - 1) % n + n,
                                    (i + 1) % n + n,
                                    (i + n) % (2 * n)]

        if D == 2:
            self.neighbor = {}

            for i in range(m):
                for j in range(n):
                    self.neighbor[i * n + j] = [(i * n + j - 1) % n + i * n,
                                                (i * n + j + 1) % n + i * n,
                                                (i * n + j - n) % (n * m),
                                                (i * n + j + n) % (n * m)]

    def sum_neighbors(self, i):
        return sum(self.state[n] for n in self.neighbor[i])

    def deltaE(self, i):
        Ei = 0
        Ef = 0
        for n in self.neighbor[i]:  # returns indices of all neighbours of ith element of a
            Ei += self.J * self.state[i] * self.state[n] / self.size
        for n in self.neighbor[i]:  # returns indices of all neighbours of ith element of a
            Ef += self.J * self.state[i] * self.state[n] / self.size
        return Ef - Ei

    def energy(self):
        E = 0
        for i in range(self.size):
            for n in self.neighbor[i]:  # returns indices of all neighbours of ith element of a
                E += self.J * self.state[i] * self.state[n] / self.size
        return E

    def deltaM(self, i):
        return (sum(self.state) - 2 * self.state[i])

    def magnetization(self):
        return sum(self.state)

    def update(self, i, dE):

        if self.T == 0:
            if dE > 0:
                p = 0
            elif dE < 0:
                p = 1
            else:
                p = 0.5
        else:
            p = 1 / (1 + math.exp(dE / self.T))

        if uniform(0, 1) <= p:
            self.state[i] = - self.state[i]
            return 1
        else:
            return 0
