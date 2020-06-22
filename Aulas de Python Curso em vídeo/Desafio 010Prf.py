real =float(input('Quanto dinheiro voce tem na carteira? R$'))
dollar = real / 3.27
euro = real / 4.85
yene = real / 0.65
peco = real / 0.31
print('Com R${:.2f} voce pode compra:\n US${:.2f}\n Er${:.2f}\n Ye${:.2f}\n Pc${:.2f}'.format(real, dollar, euro, yene, peco))

