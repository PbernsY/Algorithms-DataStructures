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

class LinkedList(object):
	def __init__(self, root = None):
		self.root = root
		self.size = 0
	def size_list(self):
		return self.size
	def add(self, data):
		new_node = Node(data, self.root)
		self.root = new_node
		self.size += 1
	def remove(self, d):
		current_node = self.root
		prev_node = None
		while current_node:
			if current_node.get_data() == d:
				if prev_node:
					prev_node.set_next_node(current_node.get_next_node())
				else:
					self.root = current_node
				self.size -= 1 
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
	
	

mylist = LinkedList()
mylist.add(5)
mylist.add(8)
mylist.add(12)
mylist.remove(8)
print(mylist.remove(12))
print(mylist.find(8))