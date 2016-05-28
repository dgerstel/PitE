#!usr/bin/env python3.2

# Exception class describing situation when invalid integration point was entered
class InvalidIntegrationPointException(Exception):
	
	def __init__(self, message):
		super(InvalidIntegrationPointException, self).__init__(message)