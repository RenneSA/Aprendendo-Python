# laços de validação simples!!!!
# VALIDAÇÃO USANDO O WHILE SEM VARIÁVEL!
# A condição de validação precisa ser ao contrario do necessário pois o laço while busca sempre verdade
'''n = int(input("Digite um número de 1 a 50: "))
while n < 1 or n > 50:
    n = int(input('Numero fora do intervalo! Digite novamente: '))
print('Numero Aceito!!!')'''

'''n = float(input('Digite um número maior que 0 (ZERO): '))
while n<= 0:
    n = int(input("Tente novamente: "))
print('Número aceito!!!')'''

# VALIDAÇÃO USANDO O WHILE, CRIANDO VARIÁVEL!!
n = int(input("Digite um número de 1 a 50: "))
n_fora = n < 1 or n > 50
while n_fora:
    n = int(input('Numero fora do intervalo! Digite novamente: '))
    n_fora = n < 1 or n > 50

print('Numero Aceito!!!') # essa mensagem pode ser trocado pelo inicio em outro código


