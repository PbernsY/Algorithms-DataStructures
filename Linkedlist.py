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

	def _sort(self):
		if self.count() > 1:
			new_list = []
			current_node = self.root
			new_list.append(current_node.data)
			while current_node.next_node:
				current_node = current_node.next_node
				new_list.append(current_node.data)
			new_list = sorted(new_list)
			sorted_ll = LinkedList()
			for i in range(len(new_list)):
				sorted_ll.add(new_list[i])
			return sorted_ll
		else:
			return []


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
	def iter_duplicates(self):
		def _iter_duplicates(ptr):
			prev = None
			while ptr and ptr.data != prev:
				prev = ptr.data
				ptr = ptr.next_node
			return ptr is not None
		return _iter_duplicates(self.root)


	def print_list(self):
		current_node = self.root
		while current_node:
			print(current_node.data)
			current_node = current_node.next_node

	def recur_print_list(self):
		def _recur_print(starting_node):
			if starting_node is None:
				return 
			else:
				print(starting_node.data)
				_recur_print(starting_node.next_node)
		return _recur_print(self.root)







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
mylist.add(100)
mylist.add(5)
mylist.add(8)
mylist.add(12)
mylist.recur_print_list()
mylist = mylist._sort()
mylist.print_list()