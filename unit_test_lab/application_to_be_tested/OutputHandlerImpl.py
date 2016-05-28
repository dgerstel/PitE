#!usr/bin/env python3.2

from OutputHandler import OutputHandler

class OutputHandlerImpl(OutputHandler):

	# Method printing info text to output
	# text - string value 
	def printInfo(self, text):
		print(text)

	# Method printing warring text to output
	# text - string value 
	def printWarrning(self, text):
		print(text)

	# Method printing error text to output
	# text - string value 
	def printError(self, text):
		print(text)
