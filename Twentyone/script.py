class scrambler:
	def __init__(self,string):
		self.string = []
		for c in string:
			self.string.append(c)

	def swapPos(self, posa, posb):
		swp = self.string[posa]
		self.string[posa] = self.string[posb]
		self.string[posb] = swp

	def swapLetter(self, lettera, letterb):
		ia = self.string.index(lettera)
		ib = self.string.index(letterb)
		self.swapPos(ia,ib)

	def rotate(self,direction,distance):
		distance = distance % len(self.string)
		if distance == 0:
			return
		rest = len(self.string) - distance
		if direction == "right":
			first = self.string[-1*distance:]
			second = self.string[:rest]
		else:
			first = self.string[-1*rest:]
			second = self.string[:distance]

		self.string = first + second

	def rotatePos(self,letter):
		amount = self.string.index(letter)
		if amount > 3:
			amount += 1
		amount += 1
		self.rotate("right", amount)

	def reverseRotatePos(self,letter):
		index = self.string.index(letter)
		amount = 1
		if index == 0:
			index += 8
		if index % 2 == 0:
			amount += index/2 + 4
		else:
			amount += (index - 1)/2
		print index
		print amount
		self.rotate("left", amount)


	def reverse(self, start,end):
		left = self.string[:start]
		center = self.string[start:end+1]
		right = self.string[end+1:]

		center.reverse()

		self.string = left + center + right

	def move(self, start, target):
		letter = self.string[start]
		self.string.remove(letter)
		self.string.insert(target, letter)

	def render(self):
		output = ""
		for l in self.string:
			output += l
		print output

s = scrambler("fbgdceah")
s.render()

with open("input.txt") as f:
	instructions = []
	for line in f:
		instructions.append(line)
	instructions.reverse()
	for line in instructions:
		line = line.strip()
		cmd, args = line.split(" ", 1)
		if cmd == "swap":
			m, x,w,m2,y = args.split(" ")
			if m == "position":
				s.swapPos(int(y),int(x))
			else:
				s.swapLetter(x,y)
		elif cmd == "rotate":
			if args[0:5] == "based":
				print "oho"
				s.reverseRotatePos(args[len(args)-1])
				#s.rotatePos(args[len(args)-1])
			else:
				direction, steps, x = args.split(" ")
				if direction == "left":
					direction = "right"
				else:
					direction = "left"
				s.rotate(direction, int(steps))
		elif cmd == "reverse":
			p, x, t , y = args.split(" ")
			s.reverse(int(x), int(y))
		elif cmd == "move":
			p, x, t , p2 ,y = args.split(" ")
			s.move(int(y),int(x))
		print cmd
		s.render()


s.render()