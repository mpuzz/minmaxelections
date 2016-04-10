from . import structures
import os.path

class Writer :
	def __init__(self, filename) :
        	self.file = open(filename, "w")

	def close(self) :
		self.file.close()

	def writesolution(self, solution) :
		self.file.write("Party;Coalition;Votes;Seats;\n")
		for x in solution.parties :
			self.file.write(x.name + ";" + x.coalition.candidate + ";" + str(x.votes) + ";" + str(solution.parties[x]) + ";\n")


