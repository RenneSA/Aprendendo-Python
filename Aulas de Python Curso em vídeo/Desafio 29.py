"""v = float(input("Qual a velocidade atual do carro? "))
limite = 80
multa = (v - limite)*7
if v > limite:
    print("Você excedeu o limite de 80km/h e foi multado em R${:.2f}".format(multa))
else:
    print("Siga sempre abaixo do limite de velocidade!!!")"""

velocidade = float(input("Qual é a celocidade atual do carro? "))
if velocidade > 80:
  print("MULTADO! Você excedeu o limite de velocidade permitido de 80km/h")
  multa = (velocidade-80)*7
  print("Você deve pagar a multa de R${:.2f}!".format(multa))
print("Tenha um bom dia! Dirija com segurança! ")
