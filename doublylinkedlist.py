class Node(object):
	def __init__(self, data, prev = None, nextn = None):
		self.data = data
		self.previous_node = prev
		self.next_node = nextn

	def get_next(self):
		return self.next_node
	def get_previous(self):
		return self.previous_node
	def set_next(self, node_instance):
		self.next_node = node_instance
	def set_previous(self, node_instance):
		self.previous_node = node_instance
	def set_data(self, _data):
		self.data = _data


class DoublyLinkedList(object):
	def __init__(self, root = None):
		self.root = root

	def insert(self, data):
		new_node = Node(data)
		if not self.root:
			self.root = new_node
		else:
			current_node = self.root
			while current_node.next_node:
				current_node = current_node.next_node
			current_node.next_node = new_node
			new_node.previous_node = current_node
	def _delete(self, data):
		current_node = self.root
		while current_node:
			if current_node.data == data:
				next_node = current_node.get_next()
				prev_node = current_node.get_previous()

				if next_node:
					next_node.set_previous(prev_node)
				if prev_node:
					prev_node.set_next(next_node)
				else:
					self.root = current_node
			else:
				current_node = current_node.get_next()
	def count(self):
		def _count(node):
			return 0 if not node else 1 + _count(node.next_node)
		return _count(self.root)




first = DoublyLinkedList()
for i in range(0, 20):
	first.insert(i)

first._delete(19)
first._delete(18)
print(first.count())
