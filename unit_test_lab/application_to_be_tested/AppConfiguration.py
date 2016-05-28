#!usr/bin/env python3.2

from InputReader import InputReader
from OutputHandler import OutputHandler
from InputValidator import InputValidator
from TrIntegrator import TrIntegrator

class AppConfiguration:

	# inputReader - InputReader derived class object
	# inputValidator - InputValidator derived class object
	# outputHandler - OutputHandler derived class object
	# trIntegrator - TrIntegrator derived class object
	def __init__(self, inputReader, inputValidator, outputHandler, trIntegrator):
		if not isinstance(inputReader, InputReader):
			raise InvalidConfigurationClass("Invalid InputReader implementation passed as argument!")
		self.inputReader = inputReader

		if not isinstance(outputHandler, OutputHandler):
			raise InvalidConfigurationClass("Invalid OutputHandler implementation passed as argument!")
		self.outputHandler = outputHandler

		if not isinstance(inputValidator, InputValidator):
			raise InvalidConfigurationClass("Invalid InputValidator implementation passed as argument!")
		self.inputValidator = inputValidator

		if not isinstance(trIntegrator, TrIntegrator):
			raise InvalidConfigurationClass("Invalid TrIntegrator implementation passed as argument!")
		self.trIntegrator = trIntegrator
