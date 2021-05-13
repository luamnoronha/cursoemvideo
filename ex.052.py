n = int(input('Digite um numero intero'))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        tot += 1
        print('\033[35m', end=' ')
    else:
        print('\033[34m', end=' ')
    print(f'{c}', end=' ')
print('\n\033[mO numero {} é divsivel por {} numeros: '.format(n, tot), end='')
if tot == 2:
    print('É primo!'.format(n), end=' ')
else:
    print('Não é primo'.format(n), end='')

