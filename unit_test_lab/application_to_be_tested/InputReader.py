#!usr/bin/env python3.2

from abc import ABCMeta, abstractmethod

class InputReader:
	__metaclass__ = ABCMeta
	
	# Abstract method returning function given by user
	@abstractmethod
	def readFunction(self):
		pass
	
	# Abstract method returning integration start point
	@abstractmethod
	def readIntegrationStart(self):
		pass

	# Abstract method returning integration end point
	@abstractmethod
	def readIntegrationEnd(self):
		pass

	# Abstract method returning integral splits ammount
	@abstractmethod
	def readSplitsAmmount(self):
		pass

