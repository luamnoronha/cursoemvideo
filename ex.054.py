import datetime
contmenor = 0
contmaior = 0
for c in range(1 ,8):
        ano = int(input('Em que ano a {}ª pessoa nasceu?'.format(c)))
        atual = datetime.date.today().year
        if atual - ano >= 21:
            contmaior += 1
        else:
            contmenor += 1
print('No total temos {} pessoas menor de idade, e {} pessoas maior de idade'.format(contmenor, contmaior))
