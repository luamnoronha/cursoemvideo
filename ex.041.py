from datetime import date
nascimento = int(input('Qual ano que você nasceu ?:'))
atual = date.today().year
idade = atual - nascimento
print('você tem {} anos.'.format(idade))
if idade <= 9:
    print('E esta na categoria MIRIM')
elif idade <= 14:
    print('E esta na categoria INFANTIL')
elif idade <= 19:
    print('E esta na categoria JUNIOR')
elif idade <= 25:
    print('E esta na categoria SENIOR')
elif idade > 25:
    print('E esta na categoria MASTER')
