preco = float(input('Preco do produto: R$'))
desc = preco*5/100
precod = preco - desc
print('Seu desconto foi de R${:.2f}\nSeu preco com desconto e R${:.2f}'.format(desc, precod))