import random
print('vamos jogar! jokempo!')
print('=='*20)
print('''escolha umas da jogadas a seguir
[1] PEDRA 
[2] TESOURA 
[3] PAPEL ''')
player = int(input('qual sua jogada: '))
opc = [1, 2, 3]
pc = random.choice(opc)
if  player == 1 and pc == 2:
    print('a jogada do pc foi TESOURA e a sua PEDRA, PARABÉNS VOCÊ É O VENCENDOR! ')
elif player == 1 and pc == 3:
    print('a jogada do PC foi PEDRA e a sua foi PAPEL, QUE PENA VOCê PERDEU!')
elif player == 1 and pc == 1:
    print('a jogada do PC foi PEDRA e a sua foi PEDRA, OPS! DEU IMPATE!')
elif player == 2 and pc == 1:
    print('a jogada do PC foi PEDRA e a sua foi TESOURA, QUE PENA VOCê PERDEU! ')
elif player == 2 and pc == 2:
    print('a jogada do PC foi TESOURA e a sua foi TESOURA, OPS! DEU IMPATE')
elif player == 2 and pc == 3:
    print('a jogada do PC foi PAPEL, e a sua foi TESOURA, PARABÉNS VOCÊ É O VENCENDOR! ')
elif player == 3 and pc == 1:
    print('a jogada do PC foi PEDRA, e a sua foi PAPEL, PARABÉNS VOCÊ É O VENCENDOR!')
elif player == 3 and pc == 2:
    print('a jogada do PC foi TESOURA, e a sua foi PAPEL, QUE PENA VOCê PERDEU! ')
elif player == 3 and pc == 3:
    print('a jogada do PC foi PAPEL e a sua foi PAPEL, OPS! DEU IMPATE')
else:
    print('comando invalido, não tente trapacear!')
