output = 0

def compare(a,b):
	res = cmp(a[1], b[1])
	if res == 0:
		return -1*cmp(a,b)
	return res
	

with open("input.txt", "r") as f:
    for line in f:
    	prefix, checksum = line.split("[")
    	
    	checksum = checksum[:5]

    	letters, secid = prefix.rsplit("-", 1)

    	secid = int(secid)
    	lettercount = {}

    	for l in letters:
    		if l in lettercount:
    			lettercount[l] += 1
    		else:
    			lettercount[l] = 1

    	lettercount["-"] = 0

    	lettercount = sorted(lettercount, cmp=lambda x,y: compare((x,lettercount[x]),(y,lettercount[y])))

    	lettercount.reverse()

    	matches = True


    	for i in range(0,4):
    		if checksum[i] != lettercount[i]:
    			matches = False

    	if matches:
    		output += secid
    		print str(checksum[0:4]) + " " + str(lettercount[0:4])

print output