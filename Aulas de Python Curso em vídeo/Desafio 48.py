'''
for c in range(3, 500, 3):
     print('{} multiplo de 3'.format(c))
print('FIM DA CONTAGEM')'''

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
        # ou cont += 1
        # ou soma += c

print('A soma de todos os {} valore solicitados é {}'.format(cont, soma))