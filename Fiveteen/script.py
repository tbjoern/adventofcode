discs = []

with open("input.txt") as f:
	for line in f:
		line = line.strip()
		line = line.split(" ")
		positions = int(line[3])
		initpos = int(line[11][:-1])
		discs.append((positions, initpos))

time = 0
done = False
while not done:
	done = True
	for i in range(len(discs)):
		if (i+1+discs[i][1]+time) % discs[i][0] != 0:
			time += 1
			done = False
			break

print time