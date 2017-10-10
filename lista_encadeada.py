class Node:

	def __init__(self, label):
		self.label = label	
		self.next = None

	def getLabel(self):
		return self.label

	def setLabel(self, label):
		return self.label

	def getNext(self):
		return self.next 

	def setNext(self, next):
		self.next = next


class LinkedList:

	def __init__(self):
		self.first = None
		self.last = None
		self.list = 0

def push(self, label, index):

	if index >= 0:
		node = Node(label)

	if self.empty():
		self.first = node
		self.last = node 
	else:

		if index == 0:
			node.setNext(self.first)
			self.first = node
		elif index >= self.len_list:

			self.last.setNext(node)
			self.last = node 
		else:
			prev_node = self.first
			curr_node = self.first.getNext()
			curr_index = 1

			while curr_node != None:

				if curr_index == index:
					node.setNext(curr_node)

					prev_node.setNext(node)
					break
				prev_node = curr_node
				curr_node = curr_node.getNext()
				curr_index += 1

			self.len_list += 1
			































