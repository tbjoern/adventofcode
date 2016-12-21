class minefield:
	def __init__(self):
		self.rows = []
		self.safetiles = 0

	def init(self,row):
		self.rows.append([])
		for tile in row:
			if tile == ".":
				self.rows[0].append(False)
			else:
				self.rows[0].append(True)

	def nextRow(self):
		self.rows.append([])
		index = len(self.rows) - 1
		for i in range(len(self.rows[0])):
			self.rows[index].append(self.isTrap(index, i))
		self.safetiles += self.countSafeTiles()
		self.rows.remove(self.rows[0])

	def isTrap(self, row, pos):
		left = self.at(row - 1, pos -1)
		center = self.at(row - 1, pos)
		right = self.at(row - 1, pos + 1)
		return (left and center and not right) or (center and right and not left) or (left and not center and not right) or (right and not center and not left)

	def at(self,row,pos):
		r = self.rows[row]
		if pos < 0 or pos >= len(r):
			return False # safe
		return self.rows[row][pos]

	def render(self):
		for row in self.rows:
			line = ""
			for r in row:
				if r:
					line += "^"
				else:
					line += "."
			print line

	def countSafeTiles(self):
		count = 0
		for tile in self.rows[0]:
			if not tile:
				count += 1
		return count

m = minefield()
row = ".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^...."
m.init(row)

#m.render()
#print

for _ in range(400000):
	m.nextRow()

#m.render()

#print
print m.safetiles
