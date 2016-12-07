file = open("input.txt", "r")

input = file.next()
sequence = input.split(", ")

class walker:
	

	def __init__(self):
		self.east = 0
		self.south = 0
		self.facing = 0
		self.tiles = {}

	def turnL(self):
		if self.facing == 0:
			self.facing = 3
		else:
			self.facing -= 1

	def turnR(self):
		if self.facing == 3:
			self.facing = 0
		else:
			self.facing += 1

	def walk(self,dist):
		for i in range(0, dist):
			if self.facing == 0:
				self.south -= 1
			elif self.facing == 1:
				self.east += 1
			elif self.facing == 2:
				self.south += 1
			else:
				self.east -= 1
			if self.kek():
				return True
			self.addTile(self.east,self.south)
		return False

	def totalDist(self):
		return abs(self.east) + abs(self.south)

	def addTile(self, x, y):
		if x in self.tiles:
			self.tiles[x].append(y)
		else:
			self.tiles[x] = [y]

	def kek(self):
		if self.east in self.tiles:
			if self.south in self.tiles[self.east]:
				return True
		return False

w = walker()

for s in sequence:
	if s[0] == "R":
		w.turnR()
	else:
		w.turnL()
	if w.walk(int(s[1:])):
		break

print w.totalDist()