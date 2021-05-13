import random
ply1 = int(input('Adivenhe um o numero: '))
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pc = random.choice(num)
while not ply1 == pc:
    if ply1 < pc:
        ply1 = int(input('um puco mais!... tente outra vez!'))
    if ply1 > pc:
        ply1 = int(input('um pouco menos!... tente outras vez!'))
print('Parabens você acertou!')
