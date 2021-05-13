termos = int(input('quantos termos vocÊ quer ver?: '))
s1 = 0
s2 = 1
print('{} → {}'.format(s1, s2), end=' ')
cont = 3
while cont <= termos:
    s3 = s1 + s2
    print('→ {}'.format(s3), end="")
    s1 = s2
    s2 = s3
    cont +=1
print('→ FIM')
