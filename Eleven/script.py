import copy
import Queue

allStates = []

def beenThereDoneThat(bf):
	h = bf.genHash()
	if h in allStates:
		return True
	return False


def equal(bf1,bf2):
	if bf1 == None or bf2 == None:
		return False
	if bf1.generators == bf2.generators and bf1.chips == bf2.chips and bf1.elevator == bf2.elevator:
		return True
	#else:
		#exchangeable = True
		#goesToEmptyFloor = False
		#for i in range(1,5):
		#	if bf1.itemsOnFloor(i) != bf2.itemsOnFloor(i):
		#		exchangeable = False
		#	if bf2.itemsOnFloor(i) == (0,0) and bf2.itemsOnFloor(i) != (0,0):
		#		goesToEmptyFloor = True
		#if exchangeable or goesToEmptyFloor:
		#	return True
	return False

class bruteforce:
	def __init__(self,gens, chips, elevator,steps,parent):
		# belegung : Pr, Co, Cu, R, Pl
		self.generators = gens
		self.chips = chips
		self.elevator = elevator
		self.nextStates = []
		self.constructs = len(gens)
		self.steps = steps
		self.parent = parent

	def itemsOnFloor(self, floor):
		gens = 0
		chips = 0
		for i in range(0,self.constructs):
			if self.generators[i] == floor:
				gens += 1
			if self.chips[i] == floor:
				chips += 1
		return (gens,chips)

	def isValid(self):
		if self.elevator < 1 or self.elevator > 4:
			return False

		#print "gens: " + str(self.generators)
		#print "chips: " + str(self.chips)
		#print "elevator: " + str(self.elevator)

		hasGen = [False,False,False,False]
		for i in range(0,4):
			if self.floorHasGenerator(i+1):
				hasGen[i] = True

		#print hasGen
		for i in range(0,self.constructs):
			if hasGen[self.chips[i] - 1] and self.chips[i] != self.generators[i]:
				#print i
				return False

		return True

	def getPossibleMoves(self):
		elements = []
		moves = []
		for i in range(0,self.constructs):
			if self.generators[i] == self.elevator:
				elements.append((i,"gen"))
			if self.chips[i] == self.elevator:
				elements.append((i,"chip"))
		for i in range(0,len(elements)):
			moves.append((elements[i], None, 1))
			moves.append((elements[i], None, -1))
			for j in range(i+1, len(elements)):
				if (elements[i][1] != elements[j][1] and elements[i][0] == elements[j][0]) or elements[i][1] == elements[j][1]:
					moves.append((elements[i], elements[j], 1))
					moves.append((elements[i], elements[j], -1))
		return moves

	def isFinal(self):
		for i in range(0,self.constructs):
			if self.generators[i] != 4 or self.chips[i] != 4:
				return False
		return True

	def createCopy(self):
		gens = copy.copy(self.generators)
		mcs = copy.copy(self.chips)
		return bruteforce(gens,mcs, self.elevator,self.steps,self)

	# builds next solution nodes
	# returns True if one of them has the final state, false otherwise
	def buildNextStates(self):
		moves = self.getPossibleMoves()
		b = self.createCopy()
		b.steps += 1

		for m in moves:
			first, second, mod = m
			if first[1] == "gen":
				b.generators[first[0]] += mod
			else:
				b.chips[first[0]] += mod
			if second != None:
				if second[1] == "gen":
					b.generators[second[0]] += mod
				else:
					b.chips[second[0]] += mod
			b.elevator += mod
			if b.isValid() and not beenThereDoneThat(b):
				self.nextStates.append(b)
				allStates.append(b.genHash())
				b = self.createCopy()
				b.steps += 1
			else:
				if first[1] == "gen":
					b.generators[first[0]] -= mod
				else:
					b.chips[first[0]] -= mod
				if second != None:
					if second[1] == "gen":
						b.generators[second[0]] -= mod
					else:
						b.chips[second[0]] -= mod
				b.elevator -= mod

		for n in self.nextStates:
			if n.isFinal():
				return n.steps

		return -1

	def floorHasGenerator(self,floor):
		return floor in self.generators

	def render(self):
		print "gens: " + str(self.generators)
		print "chips: " + str(self.chips)
		print "elevator: " + str(self.elevator)

	def genHash(self):
		return hash((str(self.generators), str(self.chips), self.elevator))

b = bruteforce([1,2,2,2,2,1,1],[1,3,3,3,3,1,1], 1, 0, None)
allStates.append(b)

q = Queue.Queue()
q.put(b)
totalsteps = -1
cur_steps = 0
while(not q.empty() and totalsteps == -1):
	item = q.get()
	#item.render()
	totalsteps = item.buildNextStates()
	for it in item.nextStates:
		q.put(it)
	#print "next states: " + str(len(item.nextStates)) + " steps: " + str(item.steps)
	if item.steps > cur_steps:
		cur_steps = item.steps
		print "cur step: " + str(cur_steps) + " queue size: " + str(q.qsize())
print totalsteps