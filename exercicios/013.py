#Algoritmo que ler o salário inicial de um funcionário 
#e mostra seu novo salário com 15% de aumento

salario = float(input('Entre com seu sálario: R$'))
aumento = salario + (salario * 15 / 100)
print('Seu novo salario, com 15% de aumento, ficou R${:.2f}'.format(aumento))