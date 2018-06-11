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
	def set_data(self, d):
		self.data = d
	def count(self):
		return 1 if not self.next_node else 1 + self.next_node.count()
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

	def remove(self, d):
		current_node = self.root
		prev_node = None
		while current_node:
			if current_node.get_data() == d:
				if prev_node:
					prev_node.set_next_node(current_node.get_next_node())
				else:
					self.root = current_node
				return True
			else:
				prev_node = current_node
				current_node = current_node.get_next_node()
		return False 
	def find(self, finder):
		current_node = self.root
		while current_node and current_node.get_data() != finder:
			current_node = current_node.get_next_node()
		return current_node

	def after(self, item):
		current_node = self.find(item)
		_value = current_node.get_next_node()
		return _value.data
	def count(self):
		return 0 if not self.root else self.root.count()
	
	

mylist = LinkedList()
mylist.add(5)
mylist.add(8)
mylist.add(12)

print(mylist.count())