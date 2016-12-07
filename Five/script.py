import hashlib

input = "ugkcyxxp"
output = ""

salt = 0

while len(output) < 8:
	hash = hashlib.md5(input + str(salt)).hexdigest()

	if hash[:5] == "00000":
		output += hash[5]
		print "got " + hash[5]

	salt +=1

print output