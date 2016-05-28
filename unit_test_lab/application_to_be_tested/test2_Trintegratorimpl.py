from TrIntegratorImpl import TrIntegratorImpl

from Integral import Integral

import unittest

EPSILON = 1e-10

class TestTrintegratorAccuracy(unittest.TestCase):
  def setUp(self):
  # create Integral instance
    self.integral = Integral
    self.integral.func = "2*x+1"
    self.integral.integrationStart = 0
    self.integral.integrationEnd = 1
    self.integral.splitsAmmount = 101

    # create TrIntegratorImpl instance
    self.trint = TrIntegratorImpl()
    self.trint.init(self.integral)

  def test_calculate_integral_return_corr_res(self):
    self.assertTrue(self.trint.calculate() - 2 < EPSILON)



if __name__ == '__main__':
  unittest.main()

