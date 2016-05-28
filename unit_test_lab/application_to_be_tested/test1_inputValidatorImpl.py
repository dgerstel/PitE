from TrIntegratorImpl import TrIntegratorImpl

from Integral import Integral

from InvalidFuncException import InvalidFuncException
from InvalidIntegrationPointException import InvalidIntegrationPointException
from InvalidIntegrationSplitsAmmountException import InvalidIntegrationSplitsAmmountException

from InputValidatorImpl import InputValidatorImpl

import unittest

EPSILON = 1e-10

class TestInputValidatorAllowedCharacters(unittest.TestCase):
  def setUp(self):
    self.inpValImpl = InputValidatorImpl()

  def testInputValidatorDoubleX(self):
     self.assertRaises(InvalidFuncException,  self.inpValImpl.validateIntegralFunc, "xx")

  def testInputValidatorLetters(self):
     self.assertRaises(InvalidFuncException,  self.inpValImpl.validateIntegralFunc, "a")

class TestInputValidatorIntegrationLimits(unittest.TestCase):
  def setUp(self):
    self.inpValImpl = InputValidatorImpl()

  def testInputValidatorIntegrationStart(self):
     self.assertRaises(InvalidIntegrationPointException, self.inpValImpl.validateIntegrationStart, "x")

  def testInputValidatorIntegrationEnd(self):
     self.assertRaises(InvalidIntegrationPointException, self.inpValImpl.validateIntegrationEnd, "3", "x")

  def testInputValidatorIntegrationRangePermutation(self):
     self.assertRaises(InvalidIntegrationPointException, self.inpValImpl.validateIntegrationEnd, "3", "2")

class TestInputValidatorSplitsAmountException(unittest.TestCase):
  def setUp(self):
    self.inpValImpl = InputValidatorImpl()

  def testInputValidatorSplitsAmountException(self):
     self.assertRaises(InvalidIntegrationSplitsAmmountException, self.inpValImpl.validateSplitsAmmount, "0")

  def testInputValidatorSplitsAmountExceptionWithCorrectInput(self):
    try:
      self.inpValImpl.validateSplitsAmmount("10")
    except InvalidIntegrationSplitsAmmountException:
      self.fail("InputValidatorImpl.validateSplitsAmmount('10') raised InvalidIntegrationSplitsAmmountException unexpectedly!")


if __name__ == '__main__':
  unittest.main()

