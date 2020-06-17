n = int(input("Digite um número de 4 a 9: "))
n_fora = n < 4 or n > 9
l = []
ana = 0
org = 0
while n_fora:
    n = int(input('Numero fora do intervalo! Digite novamente: '))
    n_fora =  n < 4 or n > 9
#print('Numero Aceito!!!') # essa mensagem pode ser trocado pelo inicio em outro código
for x in range(1, n+1):
    nome = str(input('Digite o {}º nome: '.format(x))).upper().strip()
    l.insert(x, nome)
    if x == 3:
        l.insert(3,'TESTE')
del l[2]
ana = l.count('ANA')
if ana > 0:
    print('O nome ANA aparece na posição {} da lista'.format(l.index('ANA')))
elif ana == 0:
     print('O nome ANA não existe na lista!')
org = sorted(l)
print('Alista Ordenada é {}'.format(org))