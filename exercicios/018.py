# seno, cosseno e tangente

import math
n1 = float(input('Entre com a area a ser calculada '))
sen = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tang = math.tan(math.radians(n1))
print('Seno: {:.2f} \nCosseno {:.2f} \nTangente {:.2f}'.format(sen, cos, tang))
