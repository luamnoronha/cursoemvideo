cont = 0
nomedomaisvelho = ''
masvelho = 0
somaidade = 0
for n in range(1,5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = int(input('''seu sexo:[1]F/[2]M: '''))
    somaidade += idade
    if sexo == 1 and idade < 20:
        cont +=1
    if n == 1 and sexo == 2:
        masvelho = idade
        nomedomaisvelho = nome
    if sexo == 2 and  idade > masvelho:
        masvelho = idade
        nomedomaisvelho = nome
media = somaidade/4
print('o numero de mulheres com menos de 20 anos é {}'.format(cont))
print('a media de idade do grupo é {:2}'.format(media))
print('o nome do homem mais velhor é {} e ele tem {} Anos'.format(nomedomaisvelho, masvelho))
