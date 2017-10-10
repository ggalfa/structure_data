matriz = [
	[10, 20, 30, 40],
	[50, 60, 70, 80],
	[90, 100]
]

print(matriz[1][2])
print(matriz[0][0])

vetor = [10, 20, 30, 40, 50]

print(vetor[1])


matriz_notas = [
	['jooa', 8, 7, 6],
	['pedro', 5, 6, 9]
]

for linha in matriz_notas:
	for col in linha:
		print(str(col) + '\t')