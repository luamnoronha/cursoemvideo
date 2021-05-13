print('=='*20)
print('\033[0;32mVamos calcular su imc\033[m')
print("=="*20)
altura = float(input('Qual a sua altura: '))
peso = float(input('qual seu peso: '))
imc = peso / (altura * altura)
print('O seu imc é de {:.2f}'.format(imc))
if 18.5 <= imc <= 25:
    print(' Peso ideal')
elif  imc < 18.5:
    print('esta abaixo do peso')
elif 25 < imc < 30 :
    print('esta com sobrepeso')
elif 30 < imc < 40 :
    print('esta com obesidade')
elif 40 < imc :
    print('esta com obesidade morbida')

