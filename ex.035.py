a = float(input('Primeiro seguimento'))
b = float(input('segundo seguimento'))
c = float(input('terceiro seguimento'))
if a + b > c and b + c > a and c + a > b:
    print('o triangulo existe!')
else:
    print('o trinagulo não existe!')
