#Conversão de temperatura começando com °C

tempC = float(input('Entre com a temperatura em °C'))
tempF = ((9 * tempC) / 5) + 32
tempK = tempC + 273.15

print('{:.1f}°C \n{:.1f}°F \n{:.2f}K'.format(tempC, tempF, tempK))