'''AC4 - Praticando Lógica de Programação

Faça um código em Python que:

a) Peça para o usuário digitar a quantidade de nomes que irá digitar e armazene na variável n. Essa variável n deverá ser maior que 3 e menor que 10 (Validação de dados de entrada).
 O armazenamento da variável n deverá ser feito em uma lista "l".

b) Faça as seguintes implementações, nessa ordem:

1º) Adiciona o nome "Teste" na posição 3.

2º) Exclua o elemento de índice 2.

3º) Verifique quantas vezes você digitou o nome 'Ana'. Se for maior que 0, mostre o índice da primeira ocorrência.
Se for 0, mostre uma frase informando que o nome Ana não existe na lista.

4º) No final, mostre a lista ordenada.

OBS: Carregue seu arquivo em Python em anexo a esta AC.'''



n = int(input("Digite um número de 4 a 9: "))
n_fora = n < 4 or n > 9
l = []
ana = 0
org = 0
while n_fora:
    n = int(input('Numero fora do intervalo! Digite novamente: '))
    n_fora = n < 4 or n > 9

for x in range(1, n):
    nome = str(input('Digite o {}º nome: '.format(x))).upper().strip()
    l.append(nome)

l.insert(3,'TESTE')
del l[2]
ana = l.count('ANA')
if ana > 0:
    print('O nome ANA aparece na posição {} da lista'.format(l.index('ANA')))
elif ana == 0:
     print('O nome ANA não existe na lista!')
org = sorted(l)
print('A lista Ordenada é {}'.format(org))

