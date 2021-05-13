n = int(input('digite um valor [digite 999 para parar]: '))
cont = 0
som = 0
while n != 999:
    som += n
    cont += 1
    n = int(input('digite um valor [digite 999 para parar]: '))
print('A soma dos {} numeros que você digitou é igual á {}'.format(cont,som))
