class Deque:

	def __init__(self):
		self.deque = []
		self.len = 0


	def empty(self): # verifica se esta vazia
		if self.len == 0:
			return True
		return False


	def push_front(self, e): # inserir no início
		self.deque.insert(0, e)
		self.len += 1


	def push_back(self, e): # insere no final
		self.deque.insert(self.len, e)
		self.len += 1


	def pop_front(self): # remove do inicio
		if not self.empty():
			self.deque.pop(0)
			self.len -= 1


	def pop_back(self): # remove do final
		if not self.empty():
			self.deque.pop(self.len - 1)
			self.len -= 1


	def front(self):
		if not self.empty():
			return self.deque[0]


	def back(self):
		if not self.empty():
			return self.deque[-1]


	def show(self):
		for i in self.deque:
			print(i, end=' ')



d = Deque()
d.push_front(10)
d.push_front(5)
d.push_front(20)
d.push_front(30)
d.push_back(9)
d.show()
print('\nfront: %d' % d.front())
print('back: %d' % d.back())


