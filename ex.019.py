import random
a1 = input('digite o nome do aluno1: ')
a2 = input('digite o nome do aluno2: ')
a3 = input('digite o nome do aluno3: ')
a4 = input('digite o nome do aluno4: ')
lista = [a1, a2, a3, a4]
r = random.choice(lista)
print('o aluno sorteado pra apagar o quadro é: {}'.format(r))
