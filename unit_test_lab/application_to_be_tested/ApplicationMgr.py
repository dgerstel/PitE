#!usr/bin/env python3.2

from Integral import Integral
from AppConfiguration import AppConfiguration

from InvalidFuncException import InvalidFuncException
from InvalidIntegrationPointException import InvalidIntegrationPointException
from InvalidConfigurationClass import InvalidConfigurationClass
from InvalidIntegrationSplitsAmmountException import InvalidIntegrationSplitsAmmountException

from InputReaderImpl import InputReaderImpl
from OutputHandlerImpl import OutputHandlerImpl
from InputValidatorImpl import InputValidatorImpl
from TrIntegratorImpl import TrIntegratorImpl

class ApplicationMgr:
	
	# appConfiguration - AppConfiguration class object
	def __init__(self, appConfiguration):
		self.__inputReader = appConfiguration.inputReader
		self.__inputValidator = appConfiguration.inputValidator
		self.__outputHandler = appConfiguration.outputHandler
		self.__trIntegrator = appConfiguration.trIntegrator

	# Function getting and validating integral function
	def __getAndValidateIntegralFunc(self):
		integralFunc = self.__inputReader.readFunction()
		self.__inputValidator.validateIntegralFunc(integralFunc)
		return integralFunc
	
	# Function getting and validating integration start
	def __getAndValidateIntegrationStart(self):
		integrationStart = self.__inputReader.readIntegrationStart()
		self.__inputValidator.validateIntegrationStart(integrationStart)
		return integrationStart

	# Function getting and validating integration end
	# integrationStart - integration start point
	def __getAndValidateIntegrationEnd(self, integrationStart):
		integrationEnd = self.__inputReader.readIntegrationEnd()
		self.__inputValidator.validateIntegrationEnd(integrationStart, integrationEnd)
		return integrationEnd

	# Function getting and validating integration splits ammount
	def __getAndValidateIntegrationSplitsAmmount(self):
		splitsAmmount = self.__inputReader.readSplitsAmmount()
		self.__inputValidator.validateSplitsAmmount(splitsAmmount)
		return splitsAmmount

	# Function repeating getting of integral function until it will be correct
	# integral - Integral class object
	def __initIntegralFunction(self, integral):
		try:
			self.__outputHandler.printInfo("Please enter integral function: ")
			integral.func = self.__getAndValidateIntegralFunc()
		except InvalidFuncException as e:
			self.__outputHandler.printWarrning(str(e))
			self.__initIntegralFunction(integral)

	# Function repeating getting of integration start point until it will be correct
	# integral - Integral class object
	def __initIntegrationStartPoint(self, integral):
		try:
			self.__outputHandler.printInfo("Please enter integration start point: ")
			integral.integrationStart = self.__getAndValidateIntegrationStart()
		except InvalidIntegrationPointException as e:
			self.__outputHandler.printWarrning(str(e))
			self.__initIntegrationStartPoint(integral)

	# Function repeating getting of integration start point until it will be correct
	# integral - Integral class object
	def __initIntegrationEndPoint(self, integral):
		try:
			self.__outputHandler.printInfo("Please enter integration end point: ")
			integral.integrationEnd = self.__getAndValidateIntegrationEnd(integral.integrationStart)
		except InvalidIntegrationPointException as e:
			self.__outputHandler.printWarrning(str(e))
			self.__initIntegrationEndPoint(integral)


	# Function repeating getting of integration splits ammount until it will be correct
	# integral - Integral class object
	def __initIntegrationSplitsAmmount(self, integral):
		try:
			self.__outputHandler.printInfo("Please enter ammount of integration splits: ")
			integral.splitsAmmount = self.__getAndValidateIntegrationSplitsAmmount()
		except InvalidIntegrationSplitsAmmountException as e:
			self.__outputHandler.printWarrning(str(e))
			self.__initIntegrationSplitsAmmount(integral);

	# Function handling initialization of integral func and integration points
	def __getIntegral(self):
		# Creation of new integral object
		integral = Integral()

		# Integral function
		self.__initIntegralFunction(integral)
		# Integration start
		self.__initIntegrationStartPoint(integral)
		# Integration end
		self.__initIntegrationEndPoint(integral)
		# Integration splits ammount
		self.__initIntegrationSplitsAmmount(integral)

		return integral

	# Function running program
	def run(self):
		self.__trIntegrator.init(self.__getIntegral())
		self.__outputHandler.printInfo("Integral result: " + str(self.__trIntegrator.calculate()))


# Creating app configuration
appConfiguration = AppConfiguration(InputReaderImpl(), InputValidatorImpl(), OutputHandlerImpl(), TrIntegratorImpl()) 

# Running app
ApplicationMgr(appConfiguration).run()