import math

class Party :
	def __init__(self, name, coalition,  votes, seats):
		self.name = name
		self.votes = votes
		self.seats = seats
		self.coalition = coalition

	def sethares(self, totalseats, totalvotes):
		self.minhare = int(math.floor(self.votes * float(totalseats)/totalvotes))
		self.maxhare = int(math.ceil(self.votes * float(totalseats)/totalvotes))


class Coalition :
        def __init__(self, candidate) :
                self.candidate = candidate
                self.parties = []
                self.votes = 0
                self.seats = 0

        def addParty(self, party) :
                self.parties.append(party)
                self.votes = self.votes + party.votes
                self.seats = self.seats + party.seats

	def calculatehares(self, totalseats, totalvotes):
		for party in self.parties :
			party.sethares(totalseats, totalvotes)

class Solution :
	def __init__(self) :
		self.parties = {}
		self.seatsassigned = 0

	def addparty(self, party, seats) :
		self.parties[party] = seats
		self.seatsassigned = self.seatsassigned + seats

	def clone(self) :
		newsolution = Solution()
		for key, value in self.parties.iteritems() :
			newsolution.addparty(key, value)
		return newsolution
