
class Party :
	def __init__(self, name, coalition,  votes, seats):
		self.name = name
		self.votes = votes
		self.seats = seats
		self.coalition = coalition

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
