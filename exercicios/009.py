#Tabuada

n = int(input('Digite um numero: '))
cont = 1

while cont <=10:
	print('{} x {:2} = {}'.format(n, cont, cont * n))
	cont += 1