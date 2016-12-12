import linecache
register = {"a": 0 , "b": 0, "c": 1, "d": 0}

linenumber = 1
filename = "input.txt"

def isInt(a):
	try:
		int(a)
		return True
	except ValueError, e:
		return False

def unpack(line):
	try:
		cmd, arg1, arg2 = line.split(" ")
		return True
	except ValueError:
		return False

line = linecache.getline(filename, linenumber)
while line != "":
	#print line
	if unpack(line):
		cmd, arg1, arg2 = line.split(" ")
		arg2 = arg2.strip()
	else:
		cmd, arg1 = line.split(" ")
		arg1 = arg1.strip()
	#print cmd
	#print arg1
	#print arg2
	#print f.tell()
	if cmd == "cpy":
		if isInt(arg1):
			arg1 = int(arg1)
			register[arg2] = arg1
		else:
			register[arg2] = register[arg1]
	elif cmd == "inc":
		register[arg1] += 1
	elif cmd == "dec":
		register[arg1] -= 1
	elif cmd == "jnz":
		if isInt(arg1):
			if int(arg1) != 0:
				jmpdist = int(arg2) if isInt(arg2) else register[arg2]
				#print "seeking"
				linenumber += jmpdist - 1
		elif register[arg1] != 0:
				jmpdist = int(arg2) if isInt(arg2) else register[arg2]
				#print "seeking"
				linenumber += jmpdist - 1
	linenumber += 1
	line = linecache.getline(filename, linenumber)
	#print register

print register["a"]
