"""preco = float(input("Digite o valor a ser pago R$ "))
form = int(input("Digite a forma de pagamento: 1 - Dinheiro, 2 - Cartão a vista, 3 - Cartão até 2x, 4 - Cartão mais de 3x ou 5 - Desconto diferenciado = "))

din = (-preco * 0.10) + preco
card = (-preco * 0.05) + preco
card2x = preco
card3x = (-preco * 0.30) + preco
if form == 5:
    descm = float(input("Digite o desconto diferenciado: "))
    print("Desconto DIFERENCIADO é {:.0f}% e o valor a ser pago é R${:.2f}".format(descm, (-preco * descm/100) + preco))
elif form == 1:
    print("Com pagamento em dinheiro seu desconto é de 10% e o valor fica R${:.2f}".format(din))
elif form == 2:
    print("Com pagamento em Cartão a vista seu desconto é de 5% e o valor fica R${:.2f}".format(card))
elif form == 3:
    print("Com pagamento em Cartão até 2x o valor fica R${:.2f}".format(card2x))
elif form == 4:
   print("Com pagamento em Cartão até 3x o valor fica R${:.2f}".format(card3x))"""

preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no Dinheiro ou cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a sua opção:'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total= preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Qunatas parcelas? '))
    parcela = total / totalparc
    print('Sua compra está parcelada em {} de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preco
    print('Opção de pagamento invalida. TENTE NOVAMENTE!!!')
print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(preco, total))
