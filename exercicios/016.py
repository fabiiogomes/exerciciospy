# Programa que recebe um numero real e mostre apenas sua porção inteira
from math import trunc
num = float(input('Digite um número real '))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
