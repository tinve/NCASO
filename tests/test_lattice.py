from unittest import TestCase
import sys
sys.path += ['..']
import Lattice_class

__author__ = 'galina'


class TestLattice(TestCase):
  # def test_deltaE(self):
  #   self.fail()

  def test_sum_neighbors_1D(self):
    n = 100
    m = 1
    D = 1
    J = 1
    T = 1
    lattice = Lattice_class.Lattice(n, m, D, J, T)

    for i in range(n):
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

    for i in range(n*m):
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

      # def test_deltaM(self):
      #   self.fail()
      #
      # def test_magnetization(self):
      #   self.fail()
      #
      # def test_update(self):
      #   self.fail()
