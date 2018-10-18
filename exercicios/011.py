#área de uma parede e quantidade de tinta sabendo que cada litro pinta uma área de 2m²

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
área = alt * larg
tinta = float(área / 2)
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.3f}m²'.format(larg, alt, área))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))