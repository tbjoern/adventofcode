class TLSParser:
	def __init__(self):
		self.input = ["","","",""]
		self.next = 0
		self.ready = False
		self.hypernet = False
		self.TLS = False
		self.TLSinHypernet = False

	def reset(self):
		self.ready = False
		self.next = 0
		self.hypernet = False
		self.TLS = False
		self.TLSinHypernet = False

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
				self.TLSinHypernet = self.TLSinHypernet or self.abba()
			else:
				self.TLS = self.TLS or self.abba()

	def at(self, i):
		return self.input[i%4]

	def abba(self):
		val = self.at(self.next) == self.at(self.next + 3) and self.at(self.next + 1) == self.at(self.next + 2) and self.at(self.next) != self.at(self.next + 1)

		val = val and self.ready

		return val

	def endSequence(self):
		val = self.TLS and not self.TLSinHypernet
		self.reset()
		return val

class SSLParser:
	def __init__(self):
		self.input = ["","",""]
		self.next = 0
		self.ready = False
		self.hypernet = False
		self.supernetC = []
		self.hypernetC = []

	def reset(self):
		self.next = 0
		self.ready = False
		self.hypernet = False
		self.supernetC = []
		self.hypernetC = []

	def addChar(self, c):
		if c == "[" or c == "]":
			self.ready = False
			self.next = 0
			self.hypernet = c == "["
		else:
			self.input[self.next] = c
			if self.next == 2:
				self.ready = True
				self.next = 0
			else:
				self.next += 1
		if self.ready:
			if self.aba():
				if self.hypernet:
					self.hypernetC.append(self.inOrder())
				else:
					self.supernetC.append(self.inOrder())

	def at(self, i):
		return self.input[i%3]

	def aba(self):
		return self.at(self.next) == self.at(self.next + 2) and self.at(self.next) != self.at(self.next + 1)

	def inOrder(self):
		res = []
		for i in range(self.next, self.next + 3):
			res.append(self.at(i))
		return res

	def endSequence(self):
		val = False
		for c in self.supernetC:
			inv = self.swapSequence(c)
			if inv in self.hypernetC:
				val = True
		self.reset()
		return val

	def swapSequence(self,seq):
		ret = []
		a = seq[0]
		b = seq[1]

		ret.append(b)
		ret.append(a)
		ret.append(b)

		return ret




TLS = TLSParser()
SSL = SSLParser()
output = 0

with open("input.txt", "r") as f:
	for line in f:
		for c in line:
			TLS.addChar(c)
			SSL.addChar(c)
		if SSL.endSequence():
			output += 1

print output
