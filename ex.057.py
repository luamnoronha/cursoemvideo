sexo = str(input('informe seu sexo:M/F: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Comando invalido!, informe seu sexo novamente M/F ')).strip.upper()[0]
print('sexo {} registrado'.format(sexo))
