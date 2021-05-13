print('lista de compras')
val = cont = num = menor = 0
barato = ''
while True:
    nome = str(input('Nome do produto:'))
    valor = float(input('Valor do produto: '))
    num += 1
    pro = ' '
    cont += valor
    if valor > 1000:
        val +=1
    if num == 1:
        menor = valor
        barato = nome
    else:
        if valor < menor:
            menor = valor
            barato = nome
    while pro not in 'NS':
        pro = str(input('deseja proseguir [S/N]: ')).strip().upper()[0]
    if pro == 'N':
        break
print(f'o total da sua compra foi {cont}')
print(f'Você compro {val} produtos acima de RS 1000,00')
print(f'O produto mais barato foi o {barato} e custou R${menor}')
