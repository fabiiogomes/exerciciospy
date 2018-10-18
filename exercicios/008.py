#Metros, centímetros e milimetros 

metros = float(input('Digite a quantidade de metros: '))
cm = metros * 100
mm = metros * 1000

print('{} metros \n{:.0f} centrimentos \n{:.0f} milimetros'.format(metros, cm, mm))
