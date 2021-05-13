from random import shuffle
a1 = input('digite o nome do aluno!: ')
a2 = input('digite o nome do aluno!: ')
a3 = input('digite o nome do aluno!: ')
a4 = input('digite o nome do aluno!: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('a ordem de apresentação é: ')
print(lista)
