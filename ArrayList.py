

class ArrayList():

	def __init__(self,length=0):
		self.length = length
		self.size = length*2 if length>5 else 10
		self.list = [None for i in range(self.size)]

	def get(self,index):
		if(index>=self.length or index<0):
			print("Bad index")
			return None

		return self.list[index]

	def set(self,index,value):
		if(index>=self.length or index<0):
			print("Bad index")
			return None

		self.list[index]=value

	def add(self,value,index = None):
		if(index == None):
			index = self.length
		if(self.length+1==self.size):
			#resize array
			self.size*=2
		self.list = [self.list[i] for i in range(0,index)]+[value]+[self.list[i] for i in range(index,self.length)]+[None for i in range(self.length+1,self.size)]
		self.length+=1

	def clear(self):
		self.size = 10
		self.list = [None for i in range(self.size)]
		self.length = 0

	def contains(self,value):
		for val in self.list[0:self.length]:
			if(val == value):
				return True 
		return False

	def indexOf(self,value):
		 for i,val in enumerate(self.list[0:self.length]):
		 	if(val == value):
		 		return i
		 return -1


alist = ArrayList()
alist.add(10)
alist.add(101)
alist.add(1011)
alist.add(10111)
alist.add(10)
alist.add(101)
alist.add(1011)
alist.add(10111)
alist.add(10)
print(alist.list)
alist.clear()