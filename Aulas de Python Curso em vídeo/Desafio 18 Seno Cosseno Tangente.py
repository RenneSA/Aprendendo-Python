"""import math
angulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
print("O ângulo de {} tem o SENO {:.2f} ".format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print("O ângulo de {} tem o COSSENO de{:.2f}".format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print("O ângulo de {} tem o TANGENTE de{:.2f}".format(angulo, tangente))
print()
print("O SENO é {:.2f},  o COSSENO é {:.2f} e a TANGENTE é {:.2f}".format(seno, cosseno, tangente))"""


from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(angulo))
print("O ângulo de {} tem o SENO {:.2f} ".format(angulo, seno))
cosseno = cos(radians(angulo))
print("O ângulo de {} tem o COSSENO de{:.2f}".format(angulo, cosseno))
tangente = tan(radians(angulo))
print("O ângulo de {} tem o TANGENTE de {:.2f}".format(angulo, tangente))
print()
print("O SENO é {:.2f},  o COSSENO é {:.2f} e a TANGENTE é {:.2f}".format(seno, cosseno, tangente))