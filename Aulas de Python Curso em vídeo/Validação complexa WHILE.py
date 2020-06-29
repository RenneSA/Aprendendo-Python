# Flag Boleana
# Vai validar até acertar!!!

from random import randint
'''n_secreto = randint(0, 10)
acertou = False

while not acertou:
    n = int(input('Tente Novamente'))
     if n == n_secreto:
          acertou = True
print('Você acertou ! O nuúmero era', n)'''


'''n_secreto = randint(0, 3)
n = int(input('Adivinhe o número de 0 a 3: '))
acertou = n == n_secreto

while not acertou:
    n = int(input('Tente Novamente'))
    if n == n_secreto:
        acertou = True
print('Você acertou ! O nuúmero era', n)'''


n_secreto = randint(0, 10)
acertou = False

while not acertou:
    n = int(input('Tente Novamente'))
    if n == n_secreto:
         acertou = True
print('Você acertou ! O nuúmero era', n)