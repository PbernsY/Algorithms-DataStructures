class Node(object):
	def __init__(self, data, node = None):
		self.data = data
		self.next_node = node 
	def get_next_node(self):
		return self.next_node
	def set_next_node(self, new_node_value):
		self.next_node = new_node_value
	def get_data(self):
		return self.data
	def set_data(self, data):
		self.data = data
	def __str__(self):
		return str(self.data)
class LinkedList(object):
	def __init__(self, root = None):
		self.root = root
	def size_list(self):
		return self.size
	def add(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			current_node = self.root
			while current_node.next_node:
				current_node = current_node.next_node
			current_node.next_node = Node(data)

	def remove(self, data):
		current_node = self.root
		prev_node = None
		while current_node:
			if current_node.get_data() == data:
				if prev_node:
					prev_node.set_next_node(current_node.get_next_node())
				else:
					self.root = current_node
				return True
			else:
				prev_node = current_node
				current_node = current_node.get_next_node()
		return False 
	def after(self, item):
		current_node = self.root
		while current_node and current_node.data != item:
			current_node = current_node.get_next_node()
		return None if not current_node else current_node.data

	def count(self):
		def _count(node):
			return 0 if not node else 1 + _count(node.next_node)
		return _count(self.root)


	def recur_even_elements(self):
		def _recur_even_elements(ptr, count):
			if not ptr:
				return count
			if ptr.data % 2 == 0:
				return _recur_even_elements(ptr.next_node, count + 1)
			else:
				return _recur_even_elements(ptr.next_node, count)
		return _recur_even_elements(self.root, 0)

	def recur_duplicates(self):
		def _recur_duplicates(ptr, item):
			if not ptr:
				return False
			elif ptr.data == item:
				return True
			return _recur_duplicates(ptr.next_node, ptr.data)
		return _recur_duplicates(self.root, None)

	def recur_largest(self):
		def _recur_largest(ptr, largest):
			if not ptr:
				return largest
			else:
				if ptr.data > largest:
					return _recur_largest(ptr.next_node, ptr.data)
		
				return _recur_largest(ptr.next_node, largest)
		return _recur_largest(self.root, self.root.data)





	def __len__(self):
		return self.count()


	def __getitem__(self, i):
		if i >= len(self):
			raise IndexError("LinkedList index out of range.")
		current_node = self.root
		for _ in range(i):
			current_node = current_node.next_node
		return current_node

mylist = LinkedList()
mylist.add(5)
mylist.add(5)
mylist.add(8)
mylist.add(12)
print(mylist[1])
print(mylist.recur_even_elements())
print(mylist.recur_duplicates())
print(mylist.recur_largest())
print(mylist.count())