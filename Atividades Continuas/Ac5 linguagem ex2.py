from decimal import getcontext, Decimal
getcontext().prec = 4
lista = temp = custo = []
i = 0

while True:
    compras = input()
    if compras == '0 0 0':
        break
    temp = compras.split()
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    temp[2] = float(temp[2])
    for x in range(1):
        lista.insert(x, temp)
        custo.insert(x, Decimal(temp[1]) * Decimal(temp[2]))

if not lista:
    print('nao tem compras')

else:
    codigo = custo.index(max(custo[0::2])) + 1
    print('Item mais caro')
    print(f'codigo: {custo[codigo][0]}')
    print(f'quantidade: {custo[codigo][1]}')
    print(f'Custo: {max(custo[0::2])}')



