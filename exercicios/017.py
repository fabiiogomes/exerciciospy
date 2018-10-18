# Valor da hipotenuza

from math import hypot
cato = float(input('Entre com o cateto oposto '))
cata = float(input('Entre com o cateto adjacente '))
hipot = hypot(cato, cata)

print('a hipotenuza é {:.2f}'.format(hipot))
