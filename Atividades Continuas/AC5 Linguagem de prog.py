lst = []
cod = int(input('Codigo: '))
qtd = int(input('Quantidade: '))
custo = float(input('Custo: '))
lst.append(cod)
lst.append(qtd)
lst.append(custo)
if lst.index(0) == 0 and lst.index(1) == 0 and lst.index(2) == 0:
    print('nao tem compra')
else:
   while cod != 0:
    cod = int(input('Codigo: '))
    qtd = int(input('Quantidade: '))
    custo = float(input('Custo: '))
    new_lst = []
    new_lst.append(cod)
    new_lst.append(qtd)
    new_lst.append(custo)
    print(lst)
    print(new_lst)
'''mult = lst[1]*lst[2]
print(mult)'''