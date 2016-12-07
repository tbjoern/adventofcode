class pad:
	def __init__(self):
		self.keypad =  [0,0,1,0,0,
						0,2,3,4,0,
						5,6,7,8,9,
						0,"A","B","C",0,
						0,0,"D",0,0]
		self.xpos = 0 # horizontal from left
		self.ypos = 2 # vertical from top

	def getNumber(self):
		return self.keypad[self.xpos + 5*self.ypos]

	def isKeypad(self):
		return self.getNumber() != 0

	def go(self,dir):
		if dir == "U" and self.ypos > 0:
			self.ypos -= 1
			if(not self.isKeypad()):
				self.ypos += 1
		elif dir == "D" and self.ypos < 4:
			self.ypos += 1
			if(not self.isKeypad()):
				self.ypos -= 1
		elif dir == "L" and self.xpos > 0:
			self.xpos -= 1
			if(not self.isKeypad()):
				self.xpos += 1
		elif dir == "R" and self.xpos < 4:
			self.xpos += 1
			if(not self.isKeypad()):
				self.xpos -= 1

p = pad()
output = ""

with open("input.txt", "r") as f:
    for line in f:
    	for dir in line:
    		p.go(dir)
    	output += str(p.getNumber())

print output