class Node(object):
	def __init__(self, value):
		self.value = value 
		self.front = None

class EmptyQueue(Exception):
	pass

class Queue(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0 
	def enqueue(self, value):
		new_insertion = Node(value)
		if self.tail:
			self.tail.front = new_insertion
		else:
			self.head = new_insertion

		self.tail = new_insertion
		self.count += 1
	def dequeue(self):
		if self:
			self.head = self.head.front
			self.count -= 1
		else:
			
			raise EmptyQueue()

	def first(self):
		if self:
			return self.tail.value
		else:
			raise EmptyQueue()

	def last(self):
		if self:
			return self.tail.value
		else:
			raise EmptyQueue()



queue = Queue()
for i in range(0, 20):
	queue.enqueue(i)

print(queue.first())
queue.first()

print(queue.dequeue())