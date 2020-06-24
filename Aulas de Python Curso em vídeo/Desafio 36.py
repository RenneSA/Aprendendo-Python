"""casa = (float(input("Digite o valor da casa R$ ")))
sal = float(input('Digite o Valor do salário R$ '))
ano = float(input('Digite em quantos anos quer pagar: '))
meses = ano * 12
presteca = casa / meses

if presteca >= sal*0.30:
     print('Você não pode comprar essa casa! As {:.0f} parcelas são acima de 30% do se salário R${:.2f}'.format(meses, presteca))
else:
     print('Serão {:.0f} parcelas de R${:.2f}'.format(meses, presteca))"""

casa = float(input('Valor da casa: R$: '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
     print('Emprestimo pode ser CONCEDIDO')
else:
     print('Emprestimo NEGADO')




