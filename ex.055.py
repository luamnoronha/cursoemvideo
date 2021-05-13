maior = 0
menor = 0
for c in range(1, 6):
    numero = float(input('Digite um numero: '))
    if numero == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print('O maior numero lido é {}'.format(maior))
print('o menor numero lido é {}.'.format(menor))
