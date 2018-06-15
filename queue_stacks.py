from Stack import Stack

class Queue(object):
	def __init__(self):
		self.enq_stack = Stack()
		self.deq_stack = Stack()

	def isempty(self):
		return self.enq_stack.isempty() and self.deq_stack().isempty()

	def enqueue(self, item):
		self.enq_stack.push(item)

	def dequeue(self):

		if not self.deq_stack.isempty():
			return self.deq_stack.pop()
		while not self.enq_stack.isempty():
			self.deq_stack.push(self.enq_stack.pop())
		return self.deq_stack.pop()

		