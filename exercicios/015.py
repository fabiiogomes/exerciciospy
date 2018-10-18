#Progama que ler a quantidade de dia e km de um carro alugado 
#e mostra o preço a pagar sabendo que: 1dia = R$60 e 1km = R$0,15

quantkm = float(input('Quantos Km rodados? '))
quantdia = int(input('Quantos dias alugados? '))
preço = (quantkm * 0.15) + (quantdia * 60)
print('O total a pagar é de R${:.2f}'.format(preço))