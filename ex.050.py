soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Foi informado apenas {} numeros pares a soma dos numeros é {}'.format(cont, soma))
