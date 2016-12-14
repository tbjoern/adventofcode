import hashlib
import os
import sys
import re

output = []
for i in range(0,8):
	output.append("")

hackedChars = 0

salt = "yjdafjpo"
index = 0
candidates = []
keys = {}
keys2 = []
lastIndex = 0

while len(keys) < 64:
	h = hashlib.md5(salt + hex(index)).hexdigest()

	hits = re.findall(r"([a-z0-9])\1{2}", h)
	for match in hits:
		candidates.append((match, index, h))


	for c in candidates:
		if c[1] >= index - 1000 and c[1] < index:
			matchagain = re.search("(" + c[0] + ")" + r"\1{4}", h)
			if matchagain:
				lastIndex = index
				if not c in keys:
					keys[c] = h
					keys2.append((c,h))
		elif c[1] < index - 1000:
			candidates.remove(c)

	index += 1

	if index % 20000:
		print str(index) + " " + str(len(keys)) + " " + h + " " + str(len(candidates))
print lastIndex
print len(keys)
for key in keys2:
	print key

print len(keys2)

print keys2[63]