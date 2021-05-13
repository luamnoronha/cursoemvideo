import random
from time import sleep
print('-=-'* 20)
print('vou pensar em numero de 0 a 5 tente adivinha')
print('-=-'*20)
n = int(input('pensei no numero:'))
lista = [1, 2, 3, 4, 5]
me = random.choice(lista)
print('PROCESSANDO...')
sleep(2)
if me == n:
    print('parabens você acertou! o seu numero é igual o da maquina')
else:
    print('você errou! o numero escolhido pela maquina foi {}'.format(me))


