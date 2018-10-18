#Converter real em dolar

real = float(input('Quanto dinheiro você tem? R$'))
dolar = real / 3.69
print('Olá, com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))