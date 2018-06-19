class Node():

		def __init__(self,value,next):
			self.value = value
			self.next = next

class LinkedList():

	def __init__(self):
		self.head = None
		self.length = 0

	#adds value at index
	def add(self,value,index=None):
		if(index == None):
			index = self.length
		if(index > self.length):
			print("index too high value added to end of list")
			index = self.length
		if(index < 0):
			print("index smaller then 0 value added to beggining of list")
			index = 0

		if(self.head == None):#empty list
			self.head = Node(value,None)
			self.length += 1
			return

		if(index == 0):
			tmp = self.head
			self.head = Node(value,tmp)
			return

		current_index = 0
		current = self.head
		while current_index < index-1:
			current = current.next
			current_index +=1

		tmp = current.next 
		current.next = Node(value,tmp)
		self.length += 1

	#adds the list _list to the linked list at the given index
	def add_all(self,index,_list):
		if(index > self.length):
			print("index out of bounds")
			return

		current_index = 0
		current = self.head
		while current_index < index-1:
			current = current.next
			current_index +=1

		list_index = 0

		if(index == 0):
			tmp = self.head
			self.head = Node(_list[0],tmp)
			list_index = 1
			current = self.head

		hold = current.next
		while(list_index<len(_list)):
			current.next = Node(_list[list_index],None)
			current = current.next
			list_index += 1
			self.length+=1

		current.next = hold


	#clears the list
	def clear(self):
		self.head = None
		self.length = 0

	#returns whether or not the linked list contains an element
	def contains(self,value):
		
		current = self.head
		while current.next != None:
			current = current.next
			if(current.value == value):
				return True
		return False

	#gets value at index
	def get(self,index):
		if(index < 0 or index >= self.length):
			print("index out of bounds")
			return 

		current_index = 0
		current = self.head

		while current_index < index:
			current = current.next
			current_index+=1

		return current.value

	#gets all elements in the list and returns them as a list
	def get_all(self):
		_list = []

		current = self.head
		if(self.head == None):
			return []
		while current.next != None:
			_list.append(current.value)
			current = current.next
		_list.append(current.value)
		return _list

	#sets value at index
	def set(self,value,index):
		current_index = 0
		current = self.head

		while current_index < index:
			current = current.next
			current_index+=1

		current.value = value

list_test = LinkedList()
list_test.add_all(0,[1,4,5,2,45])
list_test.add(111,0)
print(list_test.get_all())
list_test.add_all(0,[1,4,5,2,45])

print(list_test.get_all())
list_test.add(17,0)
print(list_test.get_all())
list_test.set(19,4)
list_test.add(14,0)
print(list_test.get_all())
print(list_test.contains(4))
print(list_test.length)
print(list_test.get(3))
print(list_test.get_all())
list_test.clear()
print(list_test.get_all())
