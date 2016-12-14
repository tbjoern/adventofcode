import hashlib
import re
import sys

salt = sys.argv[1] if len(sys.argv) > 1 else "abc"

def clear(lines):
		for _ in range(lines):
			sys.stdout.write("\033[F") #back to previous line
			sys.stdout.write("\033[K") #clear line

def progressBar(actual, target, width):
	bar = "< "
	percent = actual/(target*1.0)
	for i in range(width):
		if i <= percent * width:
			bar += "-"
		else:
			bar += " "
	bar += " > "
	bar += str(actual) + " of " + str(target) + " (" + str(int(percent*100)) + "%)"
	print bar

def hashPart1(salt, index):
	h = hashlib.md5(salt + str(index)).hexdigest()
	return h

def hashPart2(salt, index):
	h = hashPart1(salt, index)
	for _ in range(2016):
		h = hashlib.md5(h).hexdigest()
	return h

def solve(salt, hashfunc):
	index = 0
	candidates = []
	keys = []
	out = open("output.txt", "w")
	l = len(keys)
	progressBar(0,64,20)
	while l < 64 or len(candidates) > 0:
		h = hashfunc(salt, index)
		for c in candidates:
			if c[1] > index - 1000:
				matchagain = re.findall("(" + c[0] + ")" + r"\1{4}", h)
				if matchagain:
					out.write(str(c[1]) + "\n")
					keys.append(c)
					clear(1)
					progressBar(len(keys),64,20)
			else:
				candidates.remove(c)
		l = len(keys)

		matches = re.findall(r"(.)\1\1", h)
		if matches and l < 64:
			candidates.append((matches[0],index,h))


		index += 1
	keys.sort(key=lambda x: x[1])
	return keys

keys = solve(salt, hashPart1)
print keys[63][1]

#for k in keys:
#	print k

keys = solve(salt, hashPart2)
print keys[63][1]
