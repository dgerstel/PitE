#!usr/bin/env python3.2

from InputReader import InputReader

class InputReaderImpl(InputReader):
	
	# Method returning function given by user
	def readFunction(self):
		return input().replace("\r", "").replace("\n", "")
	
	# Method returning integration start point
	def readIntegrationStart(self):
		return input().replace("\r", "").replace("\n", "")

	# Method returning integration end point
	def readIntegrationEnd(self):
		return input().replace("\r", "").replace("\n", "")

	# Method returning integral splits ammount
	def readSplitsAmmount(self):
		return input().replace("\r", "").replace("\n", "")