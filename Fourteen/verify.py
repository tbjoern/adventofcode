muster = open("muster.txt", "r")
output = open("output.txt", "r")

mustervals = []
outputvals = []

for line in muster:
	a,b,val = line.split(" ")
	mustervals.append(int(val))

for line in output:
	outputvals.append(int(line))

print len(mustervals)
print len(outputvals)
length = min(len(mustervals), len(outputvals))

for i in range(length):
	if mustervals[i] != outputvals[i]:
		print i
		print "muster: " + str(mustervals[i])
		print "output: " + str(outputvals[i])
