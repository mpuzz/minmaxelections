#!/usr/bin/python

import sys
from datas import structures
from datas import loader
from algorithms import calculateseats
from datas import writer

def sethares(parties, votes, seats):
	for x in parties:
		x.sethares(seats, votes)

if len(sys.argv) != 2 :
	print("Usage " + sys.argv[0] + " <filename>")
	sys.exit(0)

load = loader.Loader(sys.argv[1])
coalitions = load.readFile()
load.close()

allparties = []
for x in [y.parties for y in coalitions] :
	for z in x :
		allparties.append(z)
totalseats = sum([x.seats for x in allparties])
totalvotes = sum([x.votes for x in allparties])

print("Total votes: " + str(totalvotes))
print("Total seats: " + str(totalseats))

sethares(allparties, totalvotes, totalseats)
calculator = calculateseats.Calculator(allparties, coalitions, totalseats)
calculator.haresrespectingsolution()
print(str(len(calculator.solutions)) + " solutions found")
print("Minimum error: " + str(calculator.minimizeerror()))
print(str(len(calculator.solutions)) + " solutions that minimize the error")
wr = writer.Writer("output.csv")
wr.writesolution(calculator.solutions[0])
wr.close()
