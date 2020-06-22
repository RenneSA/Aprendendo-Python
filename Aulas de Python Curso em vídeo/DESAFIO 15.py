dias = int(input("Digite a quantidade de dias: "))
km = int(input("Digite o numero de Kms Rodados: "))

pago = dias * 60 + (km*0.15)
print("O total a paga é de R${:.2f} ".format(pago))

