extenso = ('zero', 'um', 'dois','Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
  'Onze', 'Doze', 'Treze', 'Quartose', 'Quinze', 'Dezesses', 'Dezesete', 'Desoito', 'Desenove', 'Vinte')
while True:
    while True:
        n = int(input('Digite um numero de 0 a 20: '))
        if 0 <= n <= 20:
            break
        print('tente novamente!!', end=' ')
    print(f'Você digitou o numero {extenso[n]}')
    n = str(input('Você deseja continuar [s/n]?')).strip().upper()[0]
    if n == 'N':
        break

