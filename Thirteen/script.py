import sys
import time

def countBinary(x):
	ones = 0
	while (x > 0):
		if x & 1 == 1:
			ones += 1
		x = x >> 1
	return ones

def isOccupied(x,y):
	num = x*x + 3*x + 2*x*y + y + y*y
	num += 1350
	return countBinary(num) % 2 == 1

def clear():
	for i in range(height):
		sys.stdout.write("\033[F") #back to previous line
		sys.stdout.write("\033[K") #clear line

def render():
	for i in range(height):
		line = ""
		for j in range(width):
			if walls[j][i]:
				line += "#"
			elif j == 31 and i == 39:
				line += "X"
			elif (j,i) in shortestPath:
				line += "o"
			elif dist[j][i] > -1:
				line += "."
			else:
				line += " "
		print line



width, height = 40,41

walls = [[isOccupied(x,y) for y in range(height)] for x in range(width)]
input = 1350

dist = [[-1 for y in range(height)] for x in range(width)]
prev = [[None for y in range(height)] for x in range(width)]

dist[1][1] = 0

shortestPath = []

Q = []
for i in range(width):
	for j in range(height):
		if not walls[i][j]:
			Q.append((i,j))

render()
x = 0

while Q:
	min = 100000
	minq = (-1,-1)
	for q in Q:
		if dist[q[0]][q[1]] > -1 and dist[q[0]][q[1]] < min:
			min = dist[q[0]][q[1]]
			minq = q
	if minq == (-1,-1):
		break
	Q.remove(minq)
	#print len(Q)
	offset = [-1,0,1]
	for i in offset:
		for j in offset:
			offsetQ = (i+minq[0],j+minq[1])
			if i != j and j+i != 0 and offsetQ in Q:
				#print dist[i][j]
				altDist = min + 1
				if altDist < dist[offsetQ[0]][offsetQ[1]] or dist[offsetQ[0]][offsetQ[1]] == -1:
					dist[offsetQ[0]][offsetQ[1]] = altDist
					prev[offsetQ[0]][offsetQ[1]] = minq
	if x % 4 == 0:
		clear()
		render()
		time.sleep(.07)
	x += 1

shortestPath = [(31,39)]
start = (31,39)
while prev[start[0]][start[1]]:
	start = prev[start[0]][start[1]]
	shortestPath.insert(0, start)
	clear()
	render()
	time.sleep(.07)

locations = []
for i in range(width):
	for j in range(height):
		if dist[i][j] <= 50 and dist[i][j] > -1 and not (i,j) in locations:
			locations.append((i,j))

print "locations reachable: " + str(len(locations))
print "len of shortest path: " + str(len(shortestPath))