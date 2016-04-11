from datas import structures

class ThresholdCalculator :
	def __init__(self, parties, coalitions, votes) :
		self.parties = parties
		self.coalitions = coalitions
		self.totalvotes = votes

	def applythreshold(self, partyaloneth, partycoalth, coalitionth) :
		uncoalizedparties = [x.parties[0] for x in self.coalitions if len(x.parties) == 1]
		uncoalizedparties = [x for x in uncoalizedparties if float(x.votes)/self.totalvotes > partyaloneth]
		
		coalitions = [x for x in self.coalitions if float(x.votes)/self.totalvotes > coalitionth and len(x.parties) > 1]
	
		coalizedparties	= reduce(lambda x, y: x + y, [x.parties for x in coalitions])
		coalizedparties = [x for x in coalizedparties if float(x.votes)/self.totalvotes > partycoalth]

		parties =  uncoalizedparties + coalizedparties
		totalvotes = reduce(lambda x, y: x + y, [party.votes for party in parties])
		return (parties, coalitions, totalvotes)

