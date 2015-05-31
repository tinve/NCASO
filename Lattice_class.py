from __future__ import division
import math
from random import randint
from random import uniform

class Lattice:
    def __init__(self, n1, n2, n3, D, J, T):

        self.size = n1 * n2 * n3
        self.state = [2 * randint(0, 1) - 1 for i in range(n1 * n2 * n3)]

        self.D = D
        self.J = J
        self.T = T

        if D == 1 and n2 == 1 and n3 == 1:
            self.neighbors = {}
            self.coord = 2

            for i in range(n1):
                self.neighbors[i] = [(i - 1) % n1,
                                     (i + 1) % n1]

        if D == 1.5 and n2 == 2 and n3 == 1:
            self.neighbors = {}
            self.coord = 3

            for i in range(n1):
                self.neighbors[i] = [(i - 1) % n1,
                                     (i + 1) % n1,
                                     i + n1]
            for i in range(n1):
                self.neighbors[i + n1] = [(i - 1) % n1 + n1,
                                          (i + 1) % n1 + n1,
                                          i]

        if D == 2 and n3 == 1:
            self.neighbors = {}
            self.coord = 4

            for i in range(n2):
                for j in range(n1):
                    self.neighbors[i * n1 + j] = [(i * n1 + j - 1) % n1 + i * n1,
                                                  (i * n1 + j + 1) % n1 + i * n1,
                                                  (i * n1 + j - n1) % (n1 * n2),
                                                  (i * n1 + j + n1) % (n1 * n2)]

        if D == 2.5 and n3 == 2:
            self.neighbors = {}
            self.coord = 5

            for i in range(n2):
                for j in range(n1):
                    self.neighbors[i * n1 + j] = [(i * n1 + j - 1) % n1 + i * n1,
                                                  (i * n1 + j + 1) % n1 + i * n1,
                                                  (i * n1 + j - n1) % (n1 * n2),
                                                  (i * n1 + j + n1) % (n1 * n2),
                                                  i * n1 +j + n1 * n2]
            for i in range(n2):
                for j in range(n1):
                    self.neighbors[i * n1 + j + n1 * n2] = [(i * n1 + j - 1) % n1 + i * n1 + n1 * n2,
                                                            (i * n1 + j + 1) % n1 + i * n1 + n1 * n2,
                                                            (i * n1 + j - n1) % (n1 * n2) + n1 * n2,
                                                            (i * n1 + j + n1) % (n1 * n2) + n1 * n2,
                                                            i * n1 + j]


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
