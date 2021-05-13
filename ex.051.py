soma = 0
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a Razão: '))
for c in range(a1,(a1+(10 - 1 )*r) + r , r):
    print('{}'.format(c))
