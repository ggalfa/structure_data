import random

# function print aleatory number

print(random.randrange(1, 10))
print(' ')

lista = [1, 2, 3, 4, 5, 6, 7]

# sorteia um numero aleatório da lista

print(random.choice(lista))

# embaralha os numeros da lista

random.shuffle(lista)
print(lista)

print(random.sample(lista, 3))