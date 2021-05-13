casa = float(input('qual o valor do imovel?: '))
salario = float(input('qual o a sua renda mensal?: '))
anos = int(input('Quantos anos você pretende realizar?: '))
prestasao = casa / (anos * 12)
print('o valor da prestação fico em R${}'.format(prestasao))
if prestasao >= ( 0.3 * salario):
    print('\033[0;31mO seu emprestimo foi negado!')
else:
    print('\033[0;32mO seu imprestimo foi aprovado com sucesso!')

