nodes = []

class node:
	def __init__(self, coords, size, used , avail, perct):
		self.coords = coords
		self.size = int(size[:-1])
		self.used = int(used[:-1])
		self.avail = int(avail[:-1])
		self.perct = int(perct[:-1])

	def __eq__(self,other):
		return self.coords == other.coords

	def __str__(self):
		return str(self.coords) + " size: " + str(self.size) + " used: " + str(self.used) + " avail: " + str(self.avail) + " %: " + str(self.perct)

	def empty(self):
		return self.used == 0

with open("test.txt") as f:
	skip = 0
	for line in f:
		if skip < 2:
			skip += 1
			continue

		line = line.strip()
		coords, size, used , avail, perct = line.split()
		p , x , y = coords.split("-")
		n = node((int(x[1:]), int(y[1:])), size, used , avail, perct)
		nodes.append(n)
		if n.empty():
			print line
pairs = []
movable = []

for origin in nodes:
	for dest in nodes:
		if not origin.empty() and origin.used <= dest.avail and origin != dest:
			pairs.append((origin,dest))
			movable.append(origin)

print len(pairs)

width = 0
height = 0
for node in nodes:
	if node.coords[0] > width:
		width = node.coords[0]
	if node.coords[1] > height:
		height = node.coords[1]
width += 1
height += 1

grid = [[None for y in range(height)] for x in range(width)]

for node in nodes:
	mark = "#"
	if node in movable:
		mark = "."
	if node.empty():
		mark = "_"
	if node.coords[1] == 0 and node.coords[0] == width - 1:
		mark = "G"
	grid[node.coords[0]][node.coords[1]] = mark

def render(grid,shortestPath=[]):
	for j in range(height):
		output = ""
		for i in range(width):
			if (i,j) in shortestPath:
				output += "x"
			else:
				output += grid[i][j]
		print output

render(grid)

def at(grid,coords):
	return grid[coords[0]][coords[1]]

def moveLeft(grid, G, moves):
	if at(grid,G) != "G":
		moves += moveLeft(grid, (G[0] + 1, G[1]), moves)

	if at(grid, (G[0] - 1, G[1])) == ".":
		moves += makeSpace(grid,(G[0] - 1, G[1]))

	grid[G[0] - 1][G[1]] = "G"
	grid[G[0]][G[1]] = "_"
	moves += 1
	return moves

def findEmpty(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == "_":
				return (i,j)
	return (-1,-1)

def makeSpace(grid, coords):
	dist = [[-1 for y in range(height)] for x in range(width)]
	prev = [[None for y in range(height)] for x in range(width)]

	dist[coords[0]][coords[1]] = 0

	shortestPath = []

	Q = []
	for i in range(width):
		for j in range(height):
			if grid[i][j] != "#" and grid[i][j] != "G":
				Q.append((i,j))

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

	dest = findEmpty(grid)

	shortestPath = [dest]
	start = dest
	while prev[start[0]][start[1]]:
		start = prev[start[0]][start[1]]
		shortestPath.insert(0, start)

	grid[dest[0]][dest[1]] = "."
	grid[coords[0]][coords[1]] = "_"

	render(grid,shortestPath)
	print
	return len(shortestPath) - 1

print moveLeft(grid,(1,0), 0)