class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		

class SLL:
	def __init__(self):
		self.head = None
		self.tail = None
		
	def append(self, data):
		temp = Node(data)
		