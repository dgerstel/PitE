#!usr/bin/env python3.2

from abc import ABCMeta, abstractmethod

class TrIntegrator:
	__metaclass__ = ABCMeta
	
	# integral - Integral object
	def __init__(self):
		self.initialized = False

	# Abstract method calculating and returning integral value 
	@abstractmethod
	def calculate(self):
		pass

	# Method initializing trIntegrator configuration
	# integral - Integral object
	def init(self, integral):
		self.initialized = True
		self.integral = integral
	
