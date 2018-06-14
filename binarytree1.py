class Node(object):
	def __init__(self, value):
		self.value = value
		self.right_child = None
		self.left_child = None 
class BST(object):
	def __init__(self):
		self.root = None

	def add(self, data):
		def _add(node_instance):
			if not node_instance:
				return Node(data)
			if node_instance.value < data:
				node_instance.right_child = _add(node_instance.right_child)
			elif node_instance.value > data:
				node_instance.left_child = _add(node_instance.left_child)
			return node_instance
		if self.root:
		 _add(self.root)
		else:
			self.root = Node(data)


	def in_order_print(self):
		def _in_order_print(node_instance):
			if node_instance:
				_in_order_print(node_instance.left_child)
				print((node_instance.value))
				_in_order_print(node_instance.right_child)
		return(_in_order_print(self.root))



	def height1(self):
		def _height1(current_node, current_height):
			if current_node == None: return current_height
			left_height = _height1(current_node.left_child, current_height + 1)
			right_height = _height1(current_node.right_child, current_height + 1)
			return max(left_height, right_height)
		return _height1(self.root, 0)
