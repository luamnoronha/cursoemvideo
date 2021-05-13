maior = menor = media = soma = cont = 0
etc = str('s')
while etc in 'sS':
    num = int(input('Digite um numero: '))
    cont +=1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            menor = num
        if num < menor:
            menor = num
    etc = str(input('você deseja continuar [S/N]? ')).upper().strip()[0]
media = soma / cont
print('você digitou {} números e a media foi {}'.format(cont, media))
print('o maior valor é {} e o menor valor {}'.format (maior, menor))
