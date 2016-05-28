#!usr/bin/env python3.2

from abc import ABCMeta, abstractmethod

class InputValidator:
	__metaclass__ = ABCMeta

	# Abstract method validating integral function
	# function - integral function as string
	@abstractmethod
	def validateIntegralFunc(self, function):
		pass

	# Abstract method validating integration start point
	# integrationStartValue - integration start point as string
	@abstractmethod
	def validateIntegrationStart(self, integrationStartValue):
		pass

	# Abstract method validating integration end point
	# integrationStartValue - integration star point as string
	# integrationEndValue - integration end point as string
	@abstractmethod
	def validateIntegrationEnd(self, integrationStartValue, integrationEndValue):
		pass

	# Abstract method validating integration splits ammount
	# splitsAmmount - ammount of integration splits
	@abstractmethod
	def validateSplitsAmmount(self, splitsAmmount):
		pass
