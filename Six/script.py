class letterCounter:
	def __init__(self):
		self.letterMap = {}

	def incLetter(self,l):
		if l in self.letterMap:
			self.letterMap[l] += 1
		else:
			self.letterMap[l] = 1

	def mostCommon(self):
		max = 0
		letter = "-"
		for l in self.letterMap:
			if self.letterMap[l] > max:
				max = self.letterMap[l]
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
		output += c.mostCommon()
	print output