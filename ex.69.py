print('Cadastramento')
mais18 = 0
sexom = 0
sexof = 0
while True:
    idade = int(input('qual idade: '))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input('Qual sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        sexom += 1
    if sexo == 'F' and idade <= 20:
        sexof += 1
    cont = " "
    while cont not in 'SN':
        cont = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
print(f'foram cadastrada {mais18} pessoas acima de 18 anos')
print(f'Foram cadastrado {sexom} homens')
print(f'foram cadastrados o total de {sexof} de mulheres abaixo de 20 anos.')

