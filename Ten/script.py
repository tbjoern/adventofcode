class botDatabase:
	def __init__(self):
		self.bots = {}
		self.outputs = {}

	def addBot(self,id):
		if not id in self.bots:
			self.bots[id] = {"low": -1, "high": -1}

	def addOutput(self, id):
		self.outputs[id] = []

	def resetBot(self,id):
		self.bots[id]["low"] = -1
		self.bots[id]["high"] = -1

	def giveToken(self,botid, token):
		bot = self.bots[botid]
		if bot["low"] == -1:
			bot["low"] = token
		elif bot["low"] > token:
			bot["high"] = bot["low"]
			bot["low"] = token
		else:
			bot["high"] = token

	def transferSingle(self,botid,bottransfer, field):
		bot = self.bots[botid]
		self.giveToken(bottransfer, bot[field])

	def transfer(self,botid, botlowid, bothighid):
		bot = self.bots[botid]
		if(bot["low"] == 17 and bot["high"] == 61):
			print botid
		self.giveToken(botlowid,bot["low"])
		self.giveToken(bothighid,bot["high"])
		self.resetBot(botid)

	def toOuput(self, botid, outputid, field):
		self.outputs[outputid].append(self.bots[botid][field])
		self.bots[botid][field] = -1

	def render(self):
		print "bot low high"
		for bot in self.bots:
			print str(bot) + ": " + str(self.bots[bot]["low"]) + " " + str(self.bots[bot]["high"])

	def renderOutputs(self):
		print "Output Value"
		index = 0
		for o in self.outputs:
			product = 1
			for value in self.outputs[o]:
				product *= value
			print str(o) + " " + str(product)

	def checkbot(self, botid):
		bot = self.bots[botid]
		if(bot["low"] == 17 and bot["high"] == 61):
			print botid

		if bot["low"] == -1 or bot["high"] == -1:
			return False
		return True

bots = botDatabase()
instructions = []

file = open("input.txt", "r")
for line in file:
	cmd , args = line.split(" ", 1)
	if cmd == "value":
		value, x,y,z, botid = args.split(" ")
		bots.addBot(int(botid))
		bots.giveToken(int(botid), int(value))
	if cmd == "bot":
		bot, a,b,c,lowtype,botlow,e,f,g,hightype,bothigh = args.split(" ")
		bots.addBot(int(bot))
		if lowtype == "bot":
			bots.addBot(int(botlow))
		else:
			bots.addOutput(int(botlow))
		if hightype == "bot":
			bots.addBot(int(bothigh))
		else:
			bots.addOutput(int(bothigh))
		instructions.append((int(bot),lowtype, int(botlow), hightype, int(bothigh)))
file.close()
bots.render()
print
print "start transfering"

while(instructions):
	for cmd in instructions:
		bot,lowtype,botlow,hightype,bothigh = cmd
		canTransfer = bots.checkbot(int(bot))
		if canTransfer:
			if lowtype == "output":
				bots.toOuput(int(bot), int(botlow), "low")
			else:
				bots.transferSingle(int(bot), int(botlow), "low")
			if hightype == "output":
				bots.toOuput(int(bot), int(bothigh), "high")
			else:
				bots.transferSingle(int(bot), int(bothigh), "high")
			instructions.remove(cmd)
			break

print bots.renderOutputs()