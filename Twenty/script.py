ranges = []

with open("input.txt") as f:
	for line in f:
		start, end = line.split("-")
		start = int(start)
		end = int(end)
		ranges.append((start,end))
ranges.sort()

smallest = 0
count = 0
highestEnd = 0
for r in ranges:
	if r[0] <= smallest:
		if r[1] >= smallest:
			smallest = r[1] + 1
	if highestEnd < r[0] - 1:
		count += r[0] - 1 - highestEnd

	if r[1] > highestEnd:
		highestEnd = r[1]

upperBound = 4294967295
if highestEnd < upperBound:
	count += upperBound - highestEnd

print "smallest: " + str(smallest)
print "valid ips: " + str(count)