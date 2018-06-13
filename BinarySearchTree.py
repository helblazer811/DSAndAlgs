
class Node():

	def __init__(self):
		self.value = None
		self.left = None
		self.right = None

	def __init__(self,value,left,right):
		self.value = value
		self.left = left
		self.right = right


class BinaryTree():

	def __init__(self):
		self.root = None

	def insert(self,value):
		if(self.root == None):
			self.root = Node(value,None,None)
			return

		greater_than = True if value>self.root.value else False
		current_node = self.root
		next_node = self.root.left if not greater_than else self.root.right
		while next_node!=None:
			current_node = next_node
			next_node = current_node.left if not greater_than else current_node.right
			

		if greater_than:
			current_node.right = Node(value,None,None)
		else:
			current_node.left = Node(value,None,None)

	def add_all(self,values):
		if(self.root == None):
			pass		

	#gets the tree in left to right breadth first manner 
	def get_all_bf(self):
		if(self.root == None):
			return []

		class BFSQueue():

			def __init__(self):
				self.list = []
				self.length = 0

			def enqueue(self,value):
				self.list.append(value)
				self.length += 1

			def dequeue(self):
				val = self.list[0]
				self.length -= 1
				del self.list[0]
				return val 


		queue = BFSQueue()
		def bfs(root):
			vals = []
			queue.enqueue(root)

			while(queue.length != 0):
				val = queue.dequeue()
				vals.append(val.value)
				
				if(val.left != None):
					queue.enqueue(val.left)

				if(val.right != None):
					queue.enqueue(val.right)

			return vals

		return bfs(self.root)

	#gets the tree in left to right depth first manner. This should be analagous to 
	def get_all_df(self):
		if(self.root == None):
			return []	

		#this function returns a list of the inorder elements of a binary search tree
		def inorder(root):
			left = []
			right = []

			if(root.left != None):
				left = inorder(root.left)

			if(root.right != None):
				right = inorder(root.right)
				
			return left + [root.value] + right

		return inorder(self.root)

	def get(self, order):
		pass

	def size(self):
		pass

	def find_min(self):
		pass

	def find_max(self):
		pass

	def contains(self):
		pass

	#removes all elements with the given value
	def remove(self,value):
		pass

	def bfs(self):
		pass

	def dfs(self):
		pass

	#performs the avl algorithm to balance the binary tree
	def avl_balance(self):
		pass



bin_tree = BinaryTree()
bin_tree.insert(10)
bin_tree.insert(11)
bin_tree.insert(8)
bin_tree.insert(17)
bin_tree.insert(30)

print(bin_tree.get_all_df())
print(bin_tree.get_all_bf())