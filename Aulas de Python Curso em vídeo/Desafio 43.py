# CAlcular o Indice de massa muscular
"""peso = float(input("Digite o seu peso(kg): "))
alt = float(input("Digite a sua altura: "))
imc = peso / (alt ** 2)
print("Seu Índice de Massa Corporal é {:.2f}".format(imc))
if imc > 40:
    print("Obesidade Morbida")
elif imc < 18.5:
    print("Abaixo do peso")
elif imc >18.5 and imc <= 25:
    print("Peso ideal")
elif imc > 25 and imc <= 30:
    print("Sobrepeso")
elif imc > 30 and imc <= 40:
    print("Obesidade")"""

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso/ (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você Está ABAIXO DO PESO NORMAL')
elif imc <= imc < 25:
    print('PARABÉN VOCÊ ESTÁ NA FAIXA DE PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= 40:
    print('você esté em OBESIDADE, CUIDADO!!!')
elif imc >= 40:
    print('você está em OBESIDADE MORBIDA, PROCURE UM MÉDICO !!!!')


