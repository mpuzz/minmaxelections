#!/usr/bin/python

import sys
from datas import structures
from datas import loader
from algorithms import calculateseats

def sethares(parties, votes, seats):
	for x in parties:
		x.sethares(seats, votes)

if len(sys.argv) != 2 :
	print("Usage ", sys.argv[1], " <filename>")
	sys.exit(0)

load = loader.Loader("2013_elections.csv")
coalitions = load.readFile()
load.close()

allparties = []
for x in [y.parties for y in coalitions] :
	for z in x :
		allparties.append(z)
		
totalseats = sum([x.seats for x in allparties])
totalvotes = sum([x.votes for x in allparties])

print("Total votes: " + str(totalvotes))
print("Total seats " + str(totalseats))

sethares(allparties, totalvotes, totalseats)
calculator = calculateseats.Calculator(allparties, coalitions, totalseats)
calculator.haresrespectingsolution()

