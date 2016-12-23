import linecache

class interpreter:
	def __init__(self, registers, instructions):
		self.registers = registers
		self.instructions = instructions
		self.pc = 0
		self.programLength = len(instructions)

	def access(self, reg):
		try:
			return int(reg)
		except ValueError:
			return self.registers[reg]

	def set(self,reg,val):
		if self.isReg(reg):
			self.registers[reg] = val

	def isReg(self, arg):
		try:
			int(arg)
			return False
		except ValueError:
			return True

	def toggle(self, index):
		if index >= self.programLength or index < 0:
			return
		instr = self.instructions[index]
		if not instr[2]:
			if instr[0] == "inc":
				self.instructions[index] = ("dec", instr[1], instr[2])
			else:
				self.instructions[index] = ("inc", instr[1], instr[2])
		else:
			if instr[0] == "jnz":
				self.instructions[index] = ("cpy", instr[1], instr[2])
			else:
				self.instructions[index] = ("jnz", instr[1], instr[2])


	def execInstr(self,instr):
		if instr[0] == "cpy":
			self.set(instr[2], self.access(instr[1]))
		elif instr[0] == "inc":
			self.set(instr[1], self.access(instr[1]) + 1)
		elif instr[0] == "dec":
			self.set(instr[1], self.access(instr[1]) - 1)
		elif instr[0] == "jnz":
			if self.access(instr[1]) != 0:
				self.pc += self.access(instr[2])
				return
		elif instr[0] == "tgl":
			self.toggle(self.access(instr[1]) + self.pc)
		elif instr[0] == "mult":
			self.set(instr[2], self.access(instr[1]) * self.access(instr[2]))
		elif instr[0] == "add":
			self.set(instr[2], self.access(instr[1]) + self.access(instr[2]))
		self.pc += 1

	def run(self):
		while self.pc < self.programLength:
			self.execInstr(self.instructions[self.pc])

	def step(self):
		if self.pc < self.programLength:
			self.execInstr(self.instructions[self.pc])
			return True
		return False

def unpack(line):
	try:
		cmd, arg1, arg2 = line.split()
		return (cmd,arg1,arg2)
	except ValueError:
		cmd, arg1 = line.split()
		return (cmd,arg1,"")

instructions = []
with open("final.txt") as f:
	for line in f:
		instructions.append(unpack(line.strip()))

program = interpreter({"a": 12, "b": 0, "c": 0, "d": 0}, instructions)
program.run()

print program.registers
