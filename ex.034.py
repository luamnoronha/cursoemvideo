s = float(input('qual valor do seu salario?:'))
if s <= 1250:
    s1 = (s * 0.15) + s
else:
    s1 = (s * 0.1) + s
print('com o almento seu salario vai ficar {}'.format(s1))

