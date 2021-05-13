import math
a = float(input('digite um numero:'))
cos = math.cos(math.radians(a))
sen = math.sin(math.radians(a))
tan = math.tan(math.radians(a))
print('o angulo de {}, tem o cosseno de {:.2f}, o seno de {:.2f} e a tangente de {:.2f}'.format(a, cos, sen, tan))


