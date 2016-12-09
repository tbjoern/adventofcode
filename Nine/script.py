import os
from shutil import copyfile

def isNumber(c):
	try:
		int(c)
		return True
	except ValueError:
		return False

def lengthof(data, extractor):
	totallength = 0
	for c in data:
		d, times = extractor.readChar(c)
		datalength = len(d)
		if datalength > 1:
			totallength += lengthof(d,extractor) * times
		else:
			totallength += datalength * times
	return totallength

class extractor:
	def __init__(self):
		self.data = ""
		self.timesrepeat = 0
		self.datalength = 0
		self.repeating = False
		self.marker = False
		self.markerread = ""
		self.unpackedsth = False

	def readChar(self,c):
		if self.repeating:
			self.data += c
			self.datalength -= 1
			if self.datalength == 0:
				r = self.timesrepeat
				d = self.data
				self.data = ""
				self.repeating = False
				self.timesrepeat = 0
				self.unpackedsth = True
				return (d,r)
	 	elif self.marker:
	 		if c == ")":
	 			self.marker = False
	 			self.repeating = True
	 			self.timesrepeat = int(self.markerread)
	 			self.markerread = ""
	 		if isNumber(c):
	 			self.markerread += c
	 		elif c == "x":
	 			self.datalength = int(self.markerread)
	 			self.markerread = ""
	 	else:
	 		if c == "(":
	 			self.marker = True
	 		else:
	 			return (c,1)

	 	return ("",0)
	 		

e = extractor()
length = 0
fin = open("input.txt", "r")
out = open("output.txt", "w")
for line in fin:
	length += lengthof(line,e)
	#for c in line:
	#	data, times = e.readChar(c)
	#	for i in range(0,times):
	#		out.write(data)
	#		length += len(data)
print "Uncompressed has " + str(length) + " characters."
fin.close()
out.close()