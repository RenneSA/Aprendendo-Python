nome = str(input('Qual é o seu nome? '))
if nome =='Gustavo:':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é muito popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome Feminino')
print('Tenha um bom dia, {}'.format(nome))