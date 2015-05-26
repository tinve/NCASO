from __future__ import division
import math
from random import randint
from random import uniform

class Lattice:
    def __init__(self, n, m, D, J, T):

        self.size = n * m
        self.state = [2 * randint(0, 1) - 1 for i in range(n * m)]

        self.D = D
        self.J = J
        self.T = T

        if D == 1 and m == 1:
            self.neighbors = {}
            self.coord = 2

            for i in range(n):
                self.neighbors[i] = [(i - 1) % n,
                                     (i + 1) % n]

        if D == 1.5 and m == 2:
            self.neighbors = {}
            self.coord = 3

            for i in range(n):
                self.neighbors[i] = [(i - 1) % n,
                                     (i + 1) % n,
                                     (i + n) % (2 * n)]
            for i in range(n, 2 * n):
                self.neighbors[i] = [(i - 1) % n + n,
                                     (i + 1) % n + n,
                                     (i + n) % (2 * n)]

        if D == 2:
            self.neighbors = {}
            self.coord = 4

            for i in range(m):
                for j in range(n):
                    self.neighbors[i * n + j] = [(i * n + j - 1) % n + i * n,
                                                 (i * n + j + 1) % n + i * n,
                                                 (i * n + j - n) % (n * m),
                                                 (i * n + j + n) % (n * m)]

    def sum_neighbors(self, i):
        return sum(self.state[n] for n in self.neighbors[i])

    def deltaE(self, i):
        n = self.sum_neighbors(i)
        return 2 * self.J * self.state[i] * n

    def energy(self):
        E = 0
        for i, s in enumerate(self.state):
             n = self.sum_neighbors(i)
             E += - 0.5 * self.J * s * n
        return E

    def deltaM(self, i):
        return - 2 * self.state[i]

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
