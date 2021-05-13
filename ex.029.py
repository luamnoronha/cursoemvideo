v = float(input('qual a velocidade do seu carro:'))
m = (v - 80) * 7
if v <= 80 :
    print('tenha uma boa viagem')
else:
    print('você ultrapsou o limite de velocidade sua multa é de {}'.format(m))

