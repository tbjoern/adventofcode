file = open("input.txt", "r")

input = file.next()
sequence = input.split(", ")

class walker:
	

	def __init__(self):
		self.east = 0
		self.south = 0
		self.facing = 0

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
		if self.facing == 0:
			self.south -= dist
		elif self.facing == 1:
			self.east += dist
		elif self.facing == 2:
			self.south += dist
		else:
			self.east -= dist

	def totalDist(self):
		return abs(self.east) + abs(self.south)

w = walker()

for s in sequence:
	if s[0] == "R":
		w.turnR()
	else:
		w.turnL()
	print s
	w.walk(int(s[1:]))

print w.totalDist()