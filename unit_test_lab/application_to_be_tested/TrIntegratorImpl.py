#!usr/bin/env python3.2

from TrIntegrator import TrIntegrator
from InproperTrIntegratorInitializationException import InproperTrIntegratorInitializationException

class TrIntegratorImpl(TrIntegrator):
	
	# integral - Integral object
	def __init__(self):
		super(TrIntegratorImpl, self).__init__()

	# Method calculating and returning integral value 
	def calculate(self):
		if self.initialized == False:
			raise InproperTrIntegratorInitializationException("TrIntegrator object hasn't been properly initialized!")

		delta = (float(self.integral.integrationEnd) - float(self.integral.integrationStart))/int(self.integral.splitsAmmount)

		result = 0;

		x = float(self.integral.integrationStart)
		x2 = x + delta

		func2 = self.integral.func.replace("x", "(x + delta)")

		# TODO Float sci notation problem
		for i in range(0, int(self.integral.splitsAmmount)):
			result += 0.5*(eval(self.integral.func) + eval(func2))*delta
			x = x2
			x2 += delta

		return result;



