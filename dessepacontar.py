lista = (1, 2, 3, 4)

a, _, _, b = lista

print(a)
print(b)

nome = 'abc'

c1, c2, _ = nome

print(c1)
print(c2)

def func(x, y):
	return x ** 2, y ** 2

r1, r2 = func(2, 3)
print(r1)
print(r2)