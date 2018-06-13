"""
class Heap():

	def __init__(self):
		self.list = []

	def insert(self,value):
		index = 0

		if(len(self.list) == 0):
			self.list.insert(index,value)
			return
		
		next_index = 2*index+1 if value<self.list[index] else 2*index+2

		while next_index<len(self.list):
			index = next_index		
			next_index = 2*index+1 if value<self.list[index] else 2*index+2

		self.list.insert(index,value)

	def getMin(self):
		pass

	def getMax(self):
		pass

	def remove(self,index):
		pass
"""
class MaxHeap():

	def __init__(self):
		self.list = []

	def insert(self,value):
		#first add to the end of the list
		self.list.append(value)
		index = len(self.list)-1

		parent_index = index/2

		while(self.list[index]>self.list[parent_index]):
			tmp = self.list[index]
			self.list[index] = self.list[parent_index]
			self.list[parent_index] = tmp
			index = parent_index
			parent_index = index/2

	def getMax(self):
		return self.list[0]

	def remove(self):#removes the root of the heap
		#swap the value 
		ret_val = self.list[0]

		self.list[0] = self.list[len(self.list)-1]
		del self.list[len(self.list)-1]

		ind = 0
		left_bigger = self.list[ind]<self.list[2*ind+1]
		right_bigger = self.list[ind]<self.list[2*ind+2]
		while left_bigger or right_bigger:
			if(left_bigger and right_bigger):
				if(self.list[2*ind+1] > self.list[2*ind+2]):
					right_bigger = False		
				else:
					left_bigger = False
			if(left_bigger):
				tmp = self.list[2*ind+1]
				self.list[2*ind+1] = self.list[ind]
				self.list[ind] = tmp
				ind = 2*ind+1 
			else:#right  bigger
				tmp = self.list[2*ind+2]
				self.list[2*ind+2] = self.list[ind]
				self.list[ind] = tmp
				ind = 2*ind+2 
			left_bigger =2*ind+1<len(self.list) and self.list[ind]<self.list[2*ind+1]
			right_bigger = 2*ind+2<len(self.list) and self.list[ind]<self.list[2*ind+2]

		return ret_val

class MinHeap():

	def __init__(self):
		pass


max_heap = MaxHeap()
max_heap.insert(1)
max_heap.insert(2)
max_heap.insert(3)
max_heap.insert(4)
max_heap.remove()
print(max_heap.list)
