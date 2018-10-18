# ordem da apresentação
from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
ordem = shuffle(lista)
print('A ordem de apresentação será')
print(lista)
