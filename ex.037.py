num = int(input('digite um numero: '))
print('''escolha uma das bases para conversão:
[1] converte para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('sua opção: '))
if opção == 1:
    print('{} converte para BINARIO é igual a {}'.format(num, bin(num)[2:] ))
elif opção == 2:
    print('{} converte para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} converte para HEXADECIMAL a {}'.format(num, hex(num)[2:]))
else:
    print('opçaõ invalida')
