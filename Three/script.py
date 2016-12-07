class triTracker:
	def __init__(self):
		self.tri = [[],[],[]]
		self.resetTri()
		self.bitches = 0
		self.holz = 0

	def resetTri(self):
		for i in range(0,3):
			self.tri[i] = []

	def add(self, numbers):
		for i in range(0,3):
			self.tri[i].append(numbers[i])
		self.holz += 1
		if self.holz == 3:
			self.bitches += self.countValid()
			self.holz = 0
			self.resetTri()

	def countValid(self):
		alte = 0
		for stoff in self.tri:
			if self.isValid(stoff):
				alte += 1
		return alte

	def isValid(self, numbers):
		return numbers[0] + numbers[1] > numbers[2] and numbers[0] + numbers[2] > numbers[1] and numbers[2] + numbers[1] > numbers[0]

	def fuckBitches(self):
		return self.bitches

output = 0
count = 0
tri = triTracker()

with open("input.txt", "r") as f:
    for line in f:
    	numbers = line.split()
    	numbers = map(lambda x: (int(x)), numbers)

    	tri.add(numbers)

print tri.fuckBitches()