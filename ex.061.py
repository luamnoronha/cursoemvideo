a1 = int(input('digite o primeiro termo:'))
r = int(input('digite a razão: '))
termo = a1
cont = 1
while cont <= 10:
    print('{} '.format(termo), end=' ')
    termo += r
    cont += 1
print('FIM')
