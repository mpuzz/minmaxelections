from datas import structures



class Calculator :
	def __init__(self, parties, coalitions, seats):
		self.parties = sorted(parties, key=lambda x: x.votes, reverse=True)
		self.coalitions = coalitions
		self.seatstoassign = seats

	def haresrespectingsolution(self):
		self.solutions = []
		sol = structures.Solution()
		self._recursive(sol)

	def _recursive(self, solution, maxseats=2000, iteration = 0):
		if iteration == len(self.parties) :
			if solution.seatsassigned == self.seatstoassign :
				self.addsolution(solution)
		else :
			if maxseats == 0 :
				if solution.seatsassigned == self.seatstoassign :
					for x in self.parties[iteration: len(self.parties)-1] :
						solution.addparty(x, 0)
					self.addsolution(solution)
					for x in self.parties[iteration: len(self.parties)-1] :
						solution.remove(x)
				else :
					return
			else :
				for x in range(self.parties[iteration].minhare, min(self.parties[iteration].maxhare, maxseats)+1) :
					solution.addparty(self.parties[iteration], x)
					self._recursive(solution, x, iteration + 1)
					solution.remove(self.parties[iteration])
					


	def addsolution(self, solution) :
		newsolution = solution.clone()
		self.solutions.append(newsolution)
