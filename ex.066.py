cont = som = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    som += n
    cont += 1
print(f'A soma dos {cont} valores é igual á {som}')
