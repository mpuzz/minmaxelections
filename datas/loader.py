from . import structures
import os.path
import re

class Loader :
	def __init__(self, filename) :
		if os.path.exists(filename) :
			if os.path.isfile(filename) :
				self.file = open(filename, "r")
			else :
				print("Not a file")
		else :
			print("File not exists")

	def close(self) :
		self.file.close()

	def readFile(self, separator=";") :
		coalitions = []
		lines = self.file.readlines()
		coalition = None
		for line in lines :
			fields = line.split(separator)
			if len(fields) != 6 :
				continue
			if fields[0].startswith("ITALIA") :
				if fields[1] != "" :
					coalition = structures.Coalition(fields[1])
					coalitions.append(coalition)
				party = structures.Party(fields[2], coalition, int(fields[3]), int(fields[4]))
				coalition.addParty(party)
		return coalitions

if __name__ == "__main__" :
	loader = Loader("2013_elections.csv")
	print(len(loader.readFile()))
	loader.close()
