class display:
	def __init__(self,width,height):
		# store pixels in rows (screen has height many lists that are width long)
		self.screen = []
		self.width = width
		self.height = height
		for i in range(0,height):
			self.screen.append([])
			for j in range(0,width):
				self.screen[i].append(False)

	def fillRect(self, width, height):
		for i in range(0,height):
			for j in range(0,width):
				self.screen[i][j] = True

	def at(self, row, column):
		row = row % self.height
		column = column % self.width
		return self.screen[row][column]

	def shiftRow(self, row, amount):
		shift = list(self.screen[row])
		for i in range(0, self.width):
			shift[i] = self.at(row, i - amount)
		self.screen[row] = shift

	def shiftColumn(self, column, amount):
		shift = []
		for i in range(0, self.height):
			shift.append(self.screen[i][column])

		for i in range(0, self.height):
			self.screen[i][column] = shift[(i - amount) % self.height]

	def render(self):
		for row in self.screen:
			output = ""
			for pix in row:
				if pix:
					output += "#"
				else:
					output += " "
			print output

	def countLights(self):
		count = 0
		for row in self.screen:
			for pix in row:
				if pix:
					count += 1
		return count

d = display(50,6)

with open("input.txt", "r") as f:
	for line in f:
		cmd, args = line.split(" ", 1)
		if cmd == "rect":
			width, height = args.split("x")
			d.fillRect(int(width),int(height))
		elif cmd == "rotate":
			axis, index, by, amount = args.split(" ")
			index = int(index.split("=")[1])
			amount = int(amount)
			if axis == "row":
				d.shiftRow(index,amount)
			elif axis == "column":
				d.shiftColumn(index, amount)

d.render()
print d.countLights()
