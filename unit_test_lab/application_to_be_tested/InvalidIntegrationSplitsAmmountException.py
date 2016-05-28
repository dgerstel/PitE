#!usr/bin/env python3.2

# Exception class describing situation when invalid integration splits ammount value was entered
class InvalidIntegrationSplitsAmmountException(Exception):
	
	def __init__(self, message):
		super(InvalidIntegrationSplitsAmmountException, self).__init__(message)