
def soma_digitos(s):
    c = soma = 0
    lista = []
    for _ in s:
        lista.insert(c, int(n[c]))
        soma += lista[c]
        c += 1
    return soma

n = input()
print(soma_digitos(n))

