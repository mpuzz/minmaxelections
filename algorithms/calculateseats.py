from datas import structures



class Calculator :
	def __init__(self, parties, coalitions, seats):
		self.parties = parties
		self.coalitions = coalitions
		self.seatstoassigne = seats

	def haresrespectingsolution(self):
		self.solutions = []
		sol = structures.Solution()
		self._haresrecursive(sol)

	def _haresrecursive(self, solution):
		if len(solution.parties) == len(self.parties) :
			if solution.seatsassigned == self.seatstoassigne :
				self.solutions.append(solution)
		else :
			for x in range(self.parties[len(solution.parties)].minhare, 1 + self.parties[len(solution.parties)].maxhare) :
				newsolution = solution.clone()
				newsolution.addparty(self.parties[len(solution.parties)], x)
				self._haresrecursive(newsolution)


		
