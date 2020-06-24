dist = float(input("Qual A distância da sua viagem (km): "))
km = 200
if dist > km:
    print("O valor da sua viagem é R${:.2f}".format(dist*0.50))
else:
    print("O valor da sua viagem é R$:{:.2f}".format(dist*.45))
