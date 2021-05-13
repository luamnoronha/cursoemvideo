nota1 = float(input('digite a sua primeira nota:'))
nota2 = float(input('digite a sua segunda nota: '))
media = (nota1 + nota2)/2
if media >= 7:
    print('parabens sua media é {} e vc foi aprovado'.format(media))
elif 5 <= media <=6.9:
    print('voce esta na de recuperação!')
elif media < 5:
    print('você esta reprovado')
