from math import hypot
co = float(input('qual o valor do cateto oposto?: '))
ca = float(input('qual o valor do cateto adjacent?; '))
hi = hypot(co, ca)
print('se o cateto oposto é {} e o adjacente {} então a hipotenusa é {}'.format(co, ca, hi))
