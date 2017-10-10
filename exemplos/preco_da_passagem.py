"""
	viagens com uma semana de antecedencia  terao um desconto de 10% 
	e viagens com menos de 2 horas de vôo terao um desconto de 5%
	calcule o preço da passagem baseado no dia da compra e no tempo 
	de vôo.
"""
def calcular_passagem():
	precoDaPassagem = float(input("Digite o valor da passagem: "))

	diaDaCompra = int(input("Digite o dia da compra da passagem: "))

	tempoDeVoo = float(input("Digite o tempo aproximado de vôo: "))

	if diaDaCompra >= 7:
		desconto = precoDaPassagem * 0.1 

		if tempoDeVoo <= 2:
			desconto1 = precoDaPassagem * 0.05

		valor = desconto+desconto1
		print(valor)

	else:

		print("Sua passagem não tem desconto!")

	return 1
calcular_passagem()
