#!usr/bin/env python3.2

# Exception class describing situation when invalid integral function was entered
class InvalidFuncException(Exception):
	
	def __init__(self, message):
		super(InvalidFuncException, self).__init__(message)