import Queue
import time
import sys

if len(sys.argv) > 1:
	try:
		seed = int(sys.argv[1])
	except ValueError, x:
		seed = 1600

width, height = 40,41

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def isWall(x,y):
	num = x*x + 3*x + 2*x*y + y + y*y
	num += seed
	ones = 0
	while num:
		if num & 1:
			ones += 1
		num = num >> 1
	return ones % 2 == 1

def clear():
	for i in range(height):
		sys.stdout.write("\033[F") #back to previous line
		sys.stdout.write("\033[K") #clear line

def render(lab):
	for j in range(height):
		line = ""
		for i in range(width):
			if lab[i][j]:
				line += bcolors.OKBLUE + chr(176) + bcolors.ENDC
			elif (i,j) == (1,1):
				line += bcolors.FAIL + "S" + bcolors.ENDC
			elif (i,j) == (31,39):
				line += bcolors.OKGREEN + "E" + bcolors.ENDC
			elif (i,j) in shortestPath:
				line += bcolors.WARNING + "*" + bcolors.ENDC
			elif pre[i][j]:
				line += "."
			else:
				line += " "
		print line

def renderStep(skip,amount):
	if skip % amount == 0:
		clear()
		render(lab)
		time.sleep(.15)
		skip = 0
	return skip + 1

shortestPath = []

lab = [[isWall(x,y) for y in range(height)] for x in range(width)]

visited = [[False for y in range(height)] for x in range(width)]
pre = [[None for y in range(height)] for x in range(width)]

q = Queue.Queue()
q.put((1,1))

render(lab)
skip = 0

while not q.empty():
	field = q.get()

	for i in range(-1,2):
		for j in range(-1,2):
			if i != j and i + j != 0:
				adjField = (i+field[0], j + field[1])
				if adjField[0] < 0 or adjField[0] >= width or adjField[1] < 0 or adjField[1] >= height:
					continue
				if not pre[adjField[0]][adjField[1]] and not lab[adjField[0]][adjField[1]]:
					pre[adjField[0]][adjField[1]] = field
					q.put(adjField)
	skip = renderStep(skip,1)

if not pre[1][1] or not pre[31][39]:
	print "There is no path here"
	sys.exit() 

clear()
render(lab)

shortestPath = [(31,39)]
u = (31,39)
while u != (1,1):
	shortestPath.append(u)
	u = pre[u[0]][u[1]]
	skip = renderStep(skip,1)

clear()
render(lab)

print "Shortest path length: " + str(len(shortestPath))