class llnode:
	def __init__(self, value=0,prev=None, next=None):
		self.value = value
		self.prev = prev
		self.next = next

class linkedlist:
	def __init__(self):
		self.node = None

	def __init__(self,list):
		self.node = None
		for i in list:
			self.add(i)
		self.next()

	def __len__(self):
		start = self.node
		count = 1
		self.next()
		while self.node != start:
			count += 1
			self.next()
		return count

	def add(self,val):
		if self.node == None:
			self.node = llnode(val)
			self.node.next = self.node
			self.node.prev = self.node
		else:
			node = llnode(val)
			self.node.next.prev = node
			node.next = self.node.next
			self.node.next = node
			node.prev = self.node
			self.node = node

	def next(self):
		self.node = self.node.next

	def remove(self):
		prev = self.node.prev
		next = self.node.next

		self.node.prev = None
		self.node.next = None
		value = self.node.value

		self.node = next

	 	next.prev = prev
	 	prev.next = next
	 	return value

	def val(self):
	 	return self.node.value


elves = [i+1 for i in range(3005290)]
remove = False
count = len(elves)
index = 0

while count > 1:
	across = (index + count/2) % count
	elves.pop(across)
	count -= 1
	if across > index:
		index += 1
	if index >= count:
		index = 0
	if count % 10000 == 0:
		print count

print elves[0]
