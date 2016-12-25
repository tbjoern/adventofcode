import Queue
import copy
laby = []
spots = []

def isInt(c):
	try:
		int(c)
		return True
	except:
		return False

def shortestPath(map, start, dest):
	height = len(map[0])
	width = len(map)
	dist = [[-1 for y in range(height)] for x in range(width)]
	prev = [[None for y in range(height)] for x in range(width)]

	dist[start[0]][start[1]] = 0

	shortestPath = []

	Q = []
	for i in range(width):
		for j in range(height):
			if map != "#":
				Q.append((i,j))

	while dest in Q:
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

	shortestPath = [dest]
	start = dest
	while prev[start[0]][start[1]]:
		start = prev[start[0]][start[1]]
		shortestPath.insert(0, start)

	return shortestPath

zero = (1,1)

with open("test.txt") as f:
	for line in f:
		laby.append([])
		index = len(laby) - 1
		for c in line:
			laby[index].append(c)
			if isInt(c):
				spots.append((index,len(laby[index]) - 1))
				if c == 0:
					zero = (index,len(laby[index]) - 1)
distances = {}

print spots
print
print "calculating distances"

for start in spots:
	distances[start] = {}
	for dest in spots:
		if dest != start:
			distances[start][dest] = len(shortestPath(laby, start, dest) - 1)
	print "one done"

visitOrder = []
notVisited = copy.copy(spots)
start = spots[0]
notVisited.remove(start)
visitOrder.append(start)

totaldist = 0
edges = []

print distances

print "calculating mst"
while len(notVisited) > 0:
	startspot = None
	nextSpot = None
	mindist = 10000000
	for start in visitOrder:
		for dest in notVisited:
			if distances[start][dest] < mindist:
				mindist = distances[start][dest]
				nextSpot = dest
				startspot = start
	edges.append((startspot,nextSpot,mindist))
	notVisited.remove(nextSpot)
	visitOrder.append(nextSpot)
	totaldist += mindist

print totaldist
print edges

