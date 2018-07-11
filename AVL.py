## WILL BE RE WRITING MY OWN TREE SOON
## CREDIT TO @CMGN GITHUB 

class Node(object):
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right 
		self.height = 1
		self.balance_factor = 0 

	def inorder(self):
		if self.left:
			self.left.inorder()
		print(self.value)
		if self.right:
			self.right.inorder()

	def update_balance_factor(self):
		left_height = self.left.height if self.left else -1
		right_height = self.right.height if self.right else -1
		self.height = 1 + max(left_height, right_height)
		self.balance_factor = right_height - left_height

	def right_rotation(self):
		new_parent = self.left
		self.left = new_parent.right
		new_parent.right = self
		self.update_balance_factor()
		new_parent.update_balance_factor()
		return new_parent

	def left_rotation(self):
		new_parent = self.right

		self.right = new_parent.left
		new_parent.left = self
		self.update_balance_factor()
		new_parent.update_balance_factor()
		return new_parent

	def leftleft(self):
		return self.right_rotation()

	def leftright(self):
		self.left = self.left.left_rotation()
		return self.leftleft()
	def rightright(self):
		return self.left_rotation()
	def rightleft(self):
		self.right = self.right.right_rotation()
		return self.right.rightright()

	def balance(self):
		if self.balance_factor == -2:
			if self.left.balance_factor <= 0:
				return self.leftleft()
			else:
				return self.leftright()
		elif self.balance_factor == 2:
			if self.right.balance_factor >= 0:
				return self.rightright()
			else:
				return self.rightleft()

		return self


class AVLTREE(object):
	NULL_NODE = Node(None)

	def __init__(self):
		self.root = None
		self.size = 0

	def insert(self, value):
		if not self.root:
			self.root = Node(value)
			self.size = 1
			return self.root
		inserted = self._insert(self.root, value)
		if inserted is not AVLTREE.NULL_NODE:
			self.size += 1
			self.root = inserted
		return inserted




	def _insert(self, node, value):
		if node is None:
			return Node(value)
		if node.value < value:
			inserted = self._insert(node.right, value)
			if inserted is not AVLTREE.NULL_NODE:
				node.right = inserted
			else:
				return AVLTREE.NULL_NODE

		elif node.value > value:
			inserted = self._insert(node.left, value)
			if inserted is not AVLTREE.NULL_NODE:
				node.left = inserted
			else:
				return AVLTREE.NULL_NODE
		else:
			return AVLTREE.NULL_NODE

		node.update_balance_factor()
		return node.balance()

	def inorder(self):
		if self.root:
			return self.root.inorder()
		else:
			return "cant print an empty tree fuckwit"


first = AVLTREE()
for i in range(0, 20):
	first.insert(i)

first.inorder()






