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
		
	
	

mylist = LinkedList()
mylist.add(5)
mylist.add(8)
mylist.add(12)

print(mylist.count())