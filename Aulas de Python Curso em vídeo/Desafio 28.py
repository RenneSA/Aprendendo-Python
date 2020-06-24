from random import randint
from time import sleep
computador = randint(0,5)
print("--*--*--" * 20)
print("Vou pensar em um número inteiro entre 0 e 5. Tente advinhar...")
print("--*--*--" * 20)
jogador = int(input("Didite um número de 0 a 5: "))
print("PROCESSANDO.....")
sleep(1)
if jogador == computador:
    print("PARABÉNS..... Você me venceu!!! {}".format(computador))
else:
    print("Ganhei eu pensei no número {} e não no número {}!!!".format(computador, jogador))
