#!usr/bin/env python3.2

# Exception class describing situation when invalid object was passed to appManager constructor
class InvalidConfigurationClass(Exception):
	
	def __init__(self, message):
		super(InvalidConfigurationClass, self).__init__(message)