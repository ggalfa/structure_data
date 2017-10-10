"""
	criando uma classe Pessoa
	com os metodos:
	obterNome()
	obterIdade()
	setIdade()

"""


class Pessoa:

	def __init__(self, nome, idade):

		self.nome = nome
		self.idade = idade

	def obterNome(self):
		return self.nome

	def obterIdade(self):
		return self.idade

	def setIdade(self, idade):
		self.idade = idade

p1 = Pessoa('Gleison', 28)
print(p1.obterIdade())
p1.setIdade(30)
print(p1.obterIdade())
"""
p = Pessoa('Gleison', 28)
p2 = Pessoa('Amanda', 20)

pessoas = []

pessoas.append(p)
pessoas.append(p2)

for pessoa in pessoas:
	print('Nome %s' % pessoa.obterNome())
	print('Idade %d' % pessoa.obterIdade())
"""

# imprimindo numeros pares de 0 a 100.
pares = [num for num in range(101) if (num % 2 == 0)]
print(pares)


























