import random
while True:
    n = int(input('Digite um numero: '))
    pc = random.randint(0, 11)
    total = pc + n
    pi = ' '
    while pi not in "PI":
        pi = str(input('Vocé que ser Pár ou Impar (P/I): ')).strip().upper()[0]
    print(f'Você jogou {n} e o pc jogou {pc}. o total é {total}')
    if pi == 'P':
        if total % 2 == 0:
            print('Parabens vocÊ ganhou')
        else:
            print('Você perdeu!')
            break
    elif pi == 'I':
        if total % 2 == 1:
            print('Parabens vocÊ ganhou')
        else:
            print('vocÊ Perdeu!')
            break
print(f'a soma de {n} + {pc} é igual a {total} ')

