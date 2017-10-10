# descobrindo a potencia de um numero
def pot2(x):

	return x**2

pot2_ = lambda x: x**2

print(pot2_(5))

# function fatorial de number

def fat(n):
	if (n == 0):
		return 1
	return (n * fat(n - 1))

fat_ = lambda n: n * fat(n - 1) if n > 1 else 1

print('fatorial é: %d'  % fat_(5))

# map aceita mais de uma sequencia

lista = [1, 2, 3]
m = map(lambda y: y**2, lista)
for i in m:
	print(i)

# filter 

f = filter(lambda z: z%2 == 0, range(25))
for i in f:
	print(i)













