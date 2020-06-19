'''TUPLAS(que são listas imutaveis)- maneira de usar'''
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

print()
for cont in range(0, len(lanche)):
    print(lanche[cont])
print()

for  comida in enumerate(lanche):
    print(f'Eu vou comer {comida}')
print()

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

#organiza
print(sorted(lanche))
