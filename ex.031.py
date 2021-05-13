via = float(input('qual a distancia da sua viagem?:'))
v = via * 0.5
vm = via * 0.45
if via > 200:
    print('o valor de sua passagem é {:.2f}'.format(vm))
else:
    print('o valor de passagem é {:.2f}'.format(v))

