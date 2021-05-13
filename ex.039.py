from datetime import date
nascimento = int(input('Qual seu ano de nascimento: '))
atual = date.today().year
alistamento = atual - nascimento
falta = 18 - alistamento
if alistamento >  18:
    print('seu tempo de alistamento ja passou')
elif alistamento == 18:
    print('você tem que se alistar esse ano')
elif alistamento < 18:
    print('seu alistamento sera daqui a {} Anos'.format(falta))




