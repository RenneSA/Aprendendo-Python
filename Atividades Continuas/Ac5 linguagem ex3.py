num = input()
c = 0
lista = []
temp = num.split()

for x in temp:
    lista.insert(c, int((temp[c])))
    c += 1

n = 0
while n != 'final':
    n = input()
    comando = n.split()
    if 'inserir' in comando[0]:
        lista.append(int(comando[1]))
        lista.sort()
    if 'remover' in comando[0]:
        lista.remove(int(comando[1]))
    if 'parcial' in comando[0]:
        lista.sort()
        print(*lista, sep=' ')

lista.sort()
print(*lista, sep=' ')