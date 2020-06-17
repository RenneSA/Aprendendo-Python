
def contaDigtos(d):
    cont = 0
    for _ in d:
        cont += 1
    return cont


def ehBissexto(i):
    if contaDigtos(i) == 4:
        i = int(i)
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            return True
        else:
            return False


def Menssagem(z):
    if ehBissexto(z):
        z = int(z)
        atual = 2018
        if z > atual:
            print(f'O ano {z} serah bissexto')
        elif z < atual:
            print(f'O ano {z} foi bissexto')
    else:
        print(f'O ano {z} não foi bissexto')


ano = input()
year = ano.split()
for a in year:
    if contaDigtos(a) == 4:
        if ehBissexto(a):
            Menssagem(a)
        else:
            Menssagem(a)
    else:
        print('Ano inválido')
