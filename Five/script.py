import hashlib
import os
import random
import sys

input = "ugkcyxxp"
output = []
for i in range(0,8):
	output.append("")

hackedChars = 0

salt = 0
random.seed()
print

def clear():
	#os.system('cls' if os.name == 'nt' else 'clear')
	sys.stdout.write("\033[F") #back to previous line
	sys.stdout.write("\033[K") #clear line

def hacking(pwd):
	output = "0x"
	r = random.randint(40,120)
	clear()
	for c in pwd:
		if c == "":
			output += chr(((r - 30)% 80) + 40)
			r += 1
		else:
			output += c
	print output


while hackedChars < 8:
	hash = hashlib.md5(input + str(salt)).hexdigest()

	if hash[:5] == "00000":
		try:
			index = int(hash[5])
			if 0 <= index and index < 8:
				if output[index] == "":
					output[index] = hash[6]
					hacking(output)
					hackedChars += 1
		except Exception as e:
			a = 1

	salt +=1

	if salt%20000 == 0:
		hacking(output)