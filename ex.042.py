print('=='*30)
print('\033[1;32mvomos analisar a existencia e clasificação de triangulos!\033[m')
print('=='*30)
r1 = float(input('primeiro seguimento: '))
r2 = float(input('segundo seguimento: '))
r3 = float(input('terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('seu triangulo existe! E é ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    if r1!= r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Este triangulo não existe!')
