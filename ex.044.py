valor = float(input('Valor do produto: R$'))
print('''escolha um forma de pagamento 
[1] Dinheiro/cheque
[2] Á vista no cartão 
[3] 2x No cartão 
[4] Parcelado acima de 3x''')
op = int(input('sua opção: '))
if op == 1:
    print('''O valor da compra com dinheiro/cheque tem 10% de desconto, fica no total R${}'''
          .format(valor -(valor * 0.10) ))
elif op == 2:
    print('No cartão á vista você tem 5% de desconto, no total fica R${}'.format(valor - (valor *0.05)))
elif op == 3:
    parcela = valor /2
    print('O valor das parcelas sai á {}'.format(parcela))
elif op == 4:
    total = valor + (valor * 0.2)
    totalpar = int(input('Qual numero de parcelas: '))
    print('O valor da sua compra é de R${} e as {} pracelas saem á R${}'.format(total, totalpar, total/totalpar))
else:
    print('opção invalida')
