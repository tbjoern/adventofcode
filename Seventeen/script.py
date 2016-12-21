import hashlib
import Queue
import sys


passcode = "edjrjqaa" if len(sys.argv) == 1 else sys.argv[1]

pos = (0,0)
target = (4,4)
path = ""

def getDoors(pos, passcode, path):
	valid = ['b', 'c', 'd', 'e', 'f']
	md5 = hashlib.md5(passcode + path).hexdigest()

	doors = []
	for i in range(4):
		doors.append(md5[i] in valid)

	if pos[0] == 0:
		doors[2] = False
	if pos[0] == 3:
		doors[3] = False
	if pos[1] == 0:
		doors[0] = False
	if pos[1] == 3:
		doors[1] = False
	return doors

def solve(pos, passcode, path):
	doors = getDoors(pos,passcode,path)

	allPaths = []

	if doors[0]:
		allPaths.append(((pos[0], pos[1] - 1), passcode, path + "U"))
	if doors[1]:
		allPaths.append(((pos[0], pos[1] + 1), passcode, path + "D"))
	if doors[2]:
		allPaths.append(((pos[0] - 1, pos[1]), passcode, path + "L"))
	if doors[3]:
		allPaths.append(((pos[0] + 1, pos[1]), passcode, path + "R"))

	return allPaths

fields = Queue.Queue()
fields.put((pos, passcode, path))

def search(fields):
	longest = ""
	while not fields.empty():
		f = fields.get()

		nextFields = solve(f[0],f[1],f[2])
		for fi in nextFields:
			if fi[0] == (3,3):
				longest = fi[2]
			else:
				fields.put(fi)
	return longest

path = search(fields)
print len(path)