num = input()
lista = num.split()
limite = int(lista[0])
escolha = int(lista[1])
nomes = []
for x in range(limite):
    n = input()
    nomes.append(n)
nomes.sort()
escolhido = nomes[escolha - 1]
print(escolhido)

