import time
d1 = float(input('digite um numero: '))
d2 = float(input('digite um segundo numero: '))
d3 = float(input('digite o terceito e ultimo numero numero: '))
if d1 > d2 and d1 > d3:
    maior = d1
if d2 > d1 and d2 > d3:
    maior = d2
if d3 > d1 and d3 > d2:
    maior = d3
menor = d1
if d2 < d1 and d2 < d3:
    menor = d2
if d3 < d2 and d3 < d1:
    menor = d3
if d1 == d2 and d2 == d3:
    print('os numero são iguais')
else:
    print('o menor numero é: {}'.format(menor))
    print('o maior numero é: {}'.format(maior))

