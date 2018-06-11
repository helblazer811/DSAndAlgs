class ListClass():


	def __init__(self):
		self.list = []

	def set_list(self,_list):
		self.list = _list


	def insertion_sort(self):

		for i in range(1,len(self.list)):
			value = self.list[i]
			j = i-1
			while value < self.list[j] and j>=0:
				#swap values
				tmp = self.list[j]
				self.list[j]=value
				self.list[j+1]=tmp

				j=j-1


	def selection_sort(self):
		
		for i in range(len(self.list)):
			min_index = i
			for j in range(i,len(self.list)):
				if(self.list[j]<self.list[min_index]):
					min_index = j
			tmp = self.list[i]
			self.list[i] = self.list[min_index]
			self.list[min_index] = tmp

	def merge_sort(self):
		pass

	def quick_sort(self):
		pass



list_test = ListClass()
list_test.set_list([0,8,3,56,6,48,1,3])
list_test.insertion_sort()
print(list_test.list)


list_test = ListClass()
list_test.set_list([0,8,3,56,6,48,1,3])
list_test.selection_sort()
print(list_test.list)