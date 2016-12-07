class parser:
	def __init__(self):
		self.input = ["","","",""]
		self.next = 0
		self.ready = False
		self.hypernet = False
		self.valid = False
		self.invalid = False

	def reset(self):
		self.ready = False
		self.next = 0
		self.hypernet = False
		self.valid = False
		self.invalid = False

	def addChar(self, c):
		if c == "[" or c == "]":
			self.ready = False
			self.next = 0
			self.hypernet = c == "["
		else:
			self.input[self.next] = c
			if self.next == 3:
				self.ready = True
				self.next = 0
			else:
				self.next += 1
		if self.ready:
			if self.hypernet:
				self.invalid = self.invalid or self.abba()
			else:
				self.valid = self.valid or self.abba()

	def at(self, i):
		return self.input[i%4]

	def abba(self):
		val = self.at(self.next) == self.at(self.next + 3) and self.at(self.next + 1) == self.at(self.next + 2) and self.at(self.next) != self.at(self.next + 1)

		val = val and self.ready

		return val

	def endSequence(self):
		val = self.valid and not self.invalid
		self.reset()
		return val

p = parser()
output = 0

with open("input.txt", "r") as f:
	for line in f:
		for c in line:
			p.addChar(c)
		if p.endSequence():
			output += 1

print output
