nome = str(input('qual é seu nome: ')).lstrip()
separa = nome.split()
print('um momento porfavor...')
print('O seu nome em letras maisculas:{}'.format(nome.upper()))
print('o seu nome em letras minusculas:{}'.format(nome.lower()))
print('o numero de lertas que tem seu nome:{}'.format(len(nome) - nome.count(' ') ))
#print('o seu primeiro tem {} letras'.format(nome.find(' ')))
print('o seu primeiro nome é {} ele tem {} letras'.format(separa[0], len(separa[0])))












