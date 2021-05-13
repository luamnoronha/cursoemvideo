a = int(input('digite um valor: '))
b = int(input('digite outro valor :'))
print('=='*20)
opc = 0
while opc <= 4:
    print('''digite a opção que você deseja 
         [1] Somar os valore
         [2] multiplicar o valor 
         [3] Maior valor 
         [4] novos numeros
         [5] sair do programa''')
    opc = int(input('>>>>>>> sua opção: '))
    if opc == 1:
        print('a soma entre {} + {} = {}'.format(a, b, (a+b)))
    if opc == 2:
        print('a resultado da multiplicação dos numeros {} e {} é igual {}'.format(a, b, (a * b)))
    if opc == 3:
        if a > b:
            maior = a
            print('o maior valor entre {} e {} é {}'.format(a, b, maior))
        else:
            maior = b
            print('o maior valor entre {} e {} é {}'.format(a, b, maior))
    if opc == 4:
        print('informe novamente os numeros')
        a = int(input('digite um valor: '))
        b = int(input('figite outro valor: '))
    else:
        print('opção invalida')

print('programa finalizado')
