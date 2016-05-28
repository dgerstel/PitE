#!usr/bin/env python3.2

from InputValidator import InputValidator
from InvalidFuncException import InvalidFuncException
from InvalidIntegrationPointException import InvalidIntegrationPointException
from InvalidIntegrationSplitsAmmountException import InvalidIntegrationSplitsAmmountException
import re

class InputValidatorImpl(InputValidator):

	# Method validating integral function
	# function - integral function as string
	# Allows only function with set of allowed expressions: +,-,*,/,**,(,),0,1,2,3,4,5,6,7,8,9
	def validateIntegralFunc(self, function):
		if not re.match(r"[(+)(-)(*)(/)(**)(x)(\()(\))(0-9)]+", function):
			raise InvalidFuncException(function + " is invalid integral function!")

	# Method validating integration start point
	# integrationStartValue - integration start point as string
	def validateIntegrationStart(self, integrationStartValue):
		if not re.match(r"-?[0-9]+", integrationStartValue):
			raise InvalidIntegrationPointException(integrationStartValue + " is invalid integration start point!")

	# Method validating integration end point
	# integrationStartValue - integration star point as string
	# integrationEndValue - integration end point as string
	def validateIntegrationEnd(self, integrationStartValue, integrationEndValue):
		if not re.match(r"-?[0-9]+", integrationEndValue):
			raise InvalidIntegrationPointException(integrationEndValue + " is invalid integration end point!")
		if float(integrationEndValue) <= float(integrationStartValue):
			raise InvalidIntegrationPointException("Integration end point(" + str(integrationEndValue) + ") can't be lower than integration start point(" + str(integrationStartValue) + ")!")

	# Method validating integration splits ammount
	# splitsAmmount - ammount of integration splits
	def validateSplitsAmmount(self, splitsAmmount):
		if not re.match(r"[1-9][0-9]*", splitsAmmount):
			raise InvalidIntegrationSplitsAmmountException(splitsAmmount + " is invalid ammount of integration splits!")