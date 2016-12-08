class letterCounter:
	def __init__(self):
		self.letterMap = {}

	def incLetter(self,l):
		if l in self.letterMap:
			self.letterMap[l] += 1
		else:
			self.letterMap[l] = 1

	def mostCommon(self):
		return self.calcOccurence(True)

	def leastCommon(self):
		return self.calcOccurence(False)

	def calcOccurence(self, most=True):
		extremum = 0 if most else 100000
		letter = "-"
		for l in self.letterMap:
			check = self.letterMap[l] > extremum
			if not most:
				check = self.letterMap[l] < extremum
			if check:
				extremum = self.letterMap[l]
				letter = l
		return letter

with open("input.txt", "r") as f:
	fLine = f.next().strip()
	mlength = len(fLine)
	counters = []
	for i in range(0, mlength):
		counters.append(letterCounter())
	f.seek(0)
	for line in f:
		for i in range(0,mlength):
			counters[i].incLetter(line[i])

	output = ""
	for c in counters:
		output += c.leastCommon()
	print output