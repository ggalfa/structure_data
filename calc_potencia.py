"""
	algoritimo para calcular a potência de um numero.
	exp: 
	 base, exp
	 base = 2
	 exp = 10

	 2 ** 10 = 1024

"""
def pot(base, exp):

	if(exp == 0):
		return 1
	return base * pot(base, exp - 1)
print(pot(10, 2))