'''Crie um programa que leia o nome e o preço dem vários produtos. O progama deverá perguntar se o usuário vai cotinuar.
NO final, mostre:
A)Qual é o total gasto na compra.
B) Quntos Produtos custam mais de R$1000.
C Qual é o nome do produto masi barato.'''

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N} ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} custando acima de R$ 1000,00')
print(f'O pruduto mais barato foi {barato} que custa R$ {menor:.2f}')


