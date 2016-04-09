from datas import structures



class Calculator :
	def __init__(self, parties, coalitions, seats):
		self.parties = sorted(parties, key=lambda x: x.votes, reverse=True)
		self.coalitions = coalitions
		self.seatstoassigne = seats
		print([x.name for x in self.parties])

	def haresrespectingsolution(self):
		self.solutions = []
		sol = structures.Solution()
		self._recursive(sol)

	def _recursive(self, solution, maxseats=2000):
		if len(solution.parties) == len(self.parties) :
			if solution.seatsassigned == self.seatstoassigne :
				self.addsolution(solution)
		else :
			'''if maxseats == 0 :
				if solution.seatsassigned == self.seatstoassigne :
					for x in self.parties[len(solution.parties): len(self.parties)-1] :
						solution.addparty(x, 0)
					self.addsolution(solution)
				else :
					return
			else :'''
			for x in range(self.parties[len(solution.parties)].minhare, min(self.parties[len(solution.parties)].maxhare, maxseats)+1) :
				solution.addparty(self.parties[len(solution.parties)], x)
				self._recursive(solution, x)
				solution.removelast()
					


	def addsolution(self, solution) :
		for x in self.parties :
			print(x.name, x.votes, solution.parties[x])
		newsolution = solution.clone()
		self.solutions.append(newsolution)
		#if len(self.solutions) % 100 == 0 :
