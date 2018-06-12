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
	def merge_sort(self,_list):

		def sort(_list):
	
			def merge(a,b):
				out = []
				a_cnt = len(a)
				b_cnt = len(b)
				while a_cnt > 0 and b_cnt > 0:
					if(a[len(a)-a_cnt]<b[len(b)-b_cnt]):
						out.append(a[len(a)-a_cnt])
						a_cnt -= 1
					else:
						out.append(b[len(b)-b_cnt])
						b_cnt -= 1
				if(a_cnt>0):
					out = out + a[len(a)-a_cnt:]
				if(b_cnt>0):
					out = out + b[len(b)-b_cnt:]
				return out
	
			if(len(_list)==2):
				#swap if out of order
				if(_list[0]>_list[1]):
					tmp = _list[0]
					_list[0]=_list[1]
					_list[1]=tmp
				return _list

			if(len(_list)==1):
				return _list

			a = sort(_list[0:len(_list)/2])#first half
			b = sort(_list[len(_list)/2:])#second half
			return merge(a,b)

		self.list = sort(_list)

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

list_test = ListClass()
list_test.set_list([0,8,3,56,6,48,1,3])
list_test.merge_sort(list_test.list)
print(list_test.list)