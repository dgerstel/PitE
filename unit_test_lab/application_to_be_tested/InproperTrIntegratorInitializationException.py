#!usr/bin/env python3.2

# Exception class describing situation when TrIntegrator integral object hasn't been initialized properly
class InproperTrIntegratorInitializationException(Exception):
	
	def __init__(self, message):
		super(InproperTrIntegratorInitializationException, self).__init__(message)