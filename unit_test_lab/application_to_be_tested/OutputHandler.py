#!usr/bin/env python3.2

from abc import ABCMeta, abstractmethod

class OutputHandler:
	__metaclass__ = ABCMeta

	# Abstract method printing info text to output
	# text - string value 
	@abstractmethod
	def printInfo(self, text):
		pass

	# Abstract method printing warring text to output
	# text - string value 
	@abstractmethod
	def printWarrning(self, text):
		pass

	# Abstract method printing error text to output
	# text - string value 
	@abstractmethod
	def printError(self, text):
		pass
