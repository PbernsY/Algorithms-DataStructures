class Node(object):
	def __init__(self, value):
		self.value = value
		self.right_child = None
		self.left_child = None 

	def _insert(self, data):
		if self.value == data:
			return False
		elif self.value > data:
			if self.left_child:
				return self.left_child._insert(data)
			else:
				self.left_child = Node(data)
				return True
		else:
			if self.right_child:
				return self.right_child._insert(data)
			else:
				self.right_child = Node(data)
				return True

	def _print_tree(self, current_node):
		if current_node != None:
			self._print_tree(current_node.left_child)
			print(str(current_node.value))
			self._print_tree(current_node.right_child)

	def _height(self, current_node, current_height):
		if current_node == None: return current_height
		left_height = self._height(current_node.left_child, current_height + 1)
		right_height = self._height(current_node.right_child, current_height + 1)
		return max(left_height, right_height)


class BST(object):
	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root:
			return self.root._insert(value)
		else:			
			self.root = Node(value)

	def print_tree(self):
		if self.root != None:
			self.root._print_tree(self.root)


	def height(self):
		if self.root != None:
			return self.root._height(self.root, 0)
		else:
			return 0



bst = BST()

for i in range(0, 20):
	bst.insert(i)


bst.print_tree()
print(bst.height())
