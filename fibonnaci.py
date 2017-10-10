"""
	A sequencia de fibonnaci diz que os dois primeiros termos 
	são = 1 e restante a soma dos dois termos anteriores:
	ex: 1, 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8...
	temos : 1, 1, 2, 3, 5, 8...

"""

def fib(n):
	if(n == 1 or n == 2):
		return 1
	return fib(n - 1) + fib(n - 2)

print(fib(6))