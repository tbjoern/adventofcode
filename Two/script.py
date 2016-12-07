class pad:
	def __init__(self):
		self.keypad = [1,2,3,4,5,6,7,8,9]
		self.xpos = 1 # horizontal from left
		self.ypos = 1 # vertical from top

	def getNumber(self):
		return self.keypad[self.xpos + 3*self.ypos]

	def go(self,dir):
		if dir == "U" and self.ypos > 0:
			self.ypos -= 1
		elif dir == "D" and self.ypos < 2:
			self.ypos += 1
		elif dir == "L" and self.xpos > 0:
			self.xpos -= 1
		elif dir == "R" and self.xpos < 2:
			self.xpos += 1

p = pad()
output = ""

with open("input.txt", "r") as f:
    for line in f:
    	for dir in line:
    		p.go(dir)
    	output += str(p.getNumber())

print output