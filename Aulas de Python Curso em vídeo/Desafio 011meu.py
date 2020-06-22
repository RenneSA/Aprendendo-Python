lg =float(input('Inserir Largura em metros: '))
at =float(input('Inserir Altura em metros: '))
area = lg * at
print('Sua area tem a dimensao de {}x{} = {}m2\nVoce precisa de {:.2f} Litros de tinta.'.format(lg, at, area, area/2))