import copy
disklength = 35651584
state = "01000100010010111"

def lengthen(state,length):
	if length > len(state):
		extension = copy.copy(state)[::-1]
		ext2 = ""
		for c in extension:
			if c == "1":
				ext2 += "0"
			else:
				ext2 += "1"
		return lengthen(state + "0" + ext2,length)
	return state

def checksum(state, length):
	if len(state) < length:
		return "Error"
	cs = ""
	state = state[:length]
	for i in range(0,length-1,2):
		if state[i] == state[i+1]:
			cs += "1"
		else:
			cs += "0"
	if len(cs) % 2 == 1:
		return cs
	return checksum(cs, len(cs))

state = lengthen(state,disklength)
cs = checksum(state,disklength)

print cs
print len(cs)