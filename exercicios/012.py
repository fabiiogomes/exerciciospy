#Receber o preço de um produto e mostrar seu novo preço com 5% de desconto

prod = float(input('Qual o preço do produto? R$'))
desc = prod - (prod * 5 / 100)

print('O preço com desconto é {:.2f}'.format(desc))