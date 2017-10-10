#!bin/src/python3.5
#x = 0
x = int(input("Digite o valor de x: "))

y = int(input("Digite o valor de y: "))

quadrado = x * y

print(quadrado)

perimetro = (x * y) /2

print(perimetro)

if quadrado % 2 == 0:
	print("quadrado perfeito")
else:
	print("Quadrado imperfeito")