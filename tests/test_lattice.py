from unittest import TestCase
import sys
sys.path += ['..']
import Lattice_class

__author__ = 'galina'


class TestLattice(TestCase):

    def test_sum_neighbors_1D(self):
        n = 100
        m = 1
        D = 1
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        for i in range(n * m):
            sum_n = lattice.sum_neighbors(i)
            sum_n_bruteforce = sum(lattice.state[x] for x in lattice.neighbors[i])
            self.assertEqual(sum_n_bruteforce, sum_n)

    def test_sum_neighbors_1_5D(self):
        n = 50
        m = 2
        D = 1.5
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        for i in range(n * m):
            sum_n = lattice.sum_neighbors(i)
            sum_n_bruteforce = sum(lattice.state[x] for x in lattice.neighbors[i])
            self.assertEqual(sum_n_bruteforce, sum_n)

    def test_sum_neighbors_2D(self):
        n = 10
        m = 10
        D = 2
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        for i in range(n*m):
            sum_n = lattice.sum_neighbors(i)
            sum_n_bruteforce = sum(lattice.state[x] for x in lattice.neighbors[i])
            self.assertEqual(sum_n_bruteforce, sum_n)

    def test_energy_1D(self):
        n = 100
        m = 1
        D = 1
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        energy = lattice.energy()
        energy_bruteforce = 0
        for i, s in enumerate(lattice.state):
            energy_bruteforce += J * s * sum(lattice.state[n] for n in lattice.neighbors[i])
        self.assertEqual(energy_bruteforce, energy)

    def test_energy_1_5D(self):
        n = 50
        m = 2
        D = 1.5
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        energy = lattice.energy()
        energy_bruteforce = 0
        for i, s in enumerate(lattice.state):
            energy_bruteforce += J * s * sum(lattice.state[n] for n in lattice.neighbors[i])
        self.assertEqual(energy_bruteforce, energy)

    def test_energy_2D(self):
        n = 10
        m = 10
        D = 2
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        energy = lattice.energy()
        energy_bruteforce = 0
        for i, s in enumerate(lattice.state):
            energy_bruteforce += J * s * sum(lattice.state[n] for n in lattice.neighbors[i])
        self.assertEqual(energy_bruteforce, energy)

    def test_magnetization_1D(self):
        n = 100
        m = 1
        D = 1
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        magnetization = lattice.magnetization()
        magnetization_bruteforce = sum(lattice.state)
        self.assertEqual(magnetization_bruteforce, magnetization)

    def test_magnetization_1_5D(self):
        n = 50
        m = 2
        D = 1.5
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        magnetization = lattice.magnetization()
        magnetization_bruteforce = sum(lattice.state)
        self.assertEqual(magnetization_bruteforce, magnetization)

    def test_magnetization_2D(self):
        n = 10
        m = 10
        D = 2
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        magnetization = lattice.magnetization()
        magnetization_bruteforce = sum(lattice.state)
        self.assertEqual(magnetization_bruteforce, magnetization)

    def test_deltaM_1D(self):
        n = 100
        m = 1
        D = 1
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        for i in range(n * m):
            dM = lattice.deltaM(i)
            dM_bruteforce = -2 * lattice.state[i]
            self.assertEqual(dM_bruteforce, dM)

    def test_deltaM_1_5D(self):
        n = 50
        m = 2
        D = 1
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        for i in range(n * m):
            dM = lattice.deltaM(i)
            dM_bruteforce = -2 * lattice.state[i]
            self.assertEqual(dM_bruteforce, dM)

    def test_deltaM_2D(self):
        n = 10
        m = 10
        D = 2
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        for i in range(n * m):
            dM = lattice.deltaM(i)
            dM_bruteforce = -2 * lattice.state[i]
            self.assertEqual(dM_bruteforce, dM)

    def test_deltaE_1D(self):
        n = 100
        m = 1
        D = 1
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        for i in range(n * m):
            dE = lattice.deltaE(i)
            dE_bruteforce = J * lattice.state[i] * sum(lattice.state[n] for n in lattice.neighbors[i])
            self.assertEqual(dE_bruteforce, dE)

    def test_deltaE_1_5D(self):
        n = 50
        m = 2
        D = 1.5
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        for i in range(n * m):
            dE = lattice.deltaE(i)
            dE_bruteforce = J * lattice.state[i] * sum(lattice.state[n] for n in lattice.neighbors[i])
            self.assertEqual(dE_bruteforce, dE)

    def test_deltaE_2D(self):
        n = 10
        m = 10
        D = 2
        J = 1
        T = 1
        lattice = Lattice_class.Lattice(n, m, D, J, T)

        for i in range(n * m):
            dE = lattice.deltaE(i)
            dE_bruteforce = J * lattice.state[i] * sum(lattice.state[n] for n in lattice.neighbors[i])
            self.assertEqual(dE_bruteforce, dE)
#
# def test_update(self):
#   self.fail()
