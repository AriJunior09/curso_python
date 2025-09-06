# Operadores Lógicos
# in e not in

# Strings são interaveis

#..0.1.2.3.4.5
#..O.t.á.v.i.o
#.-6-5-4-3-2-1

nome = 'Otávio'
# print(nome[2])
# print(nome[-4])

# print('á' in nome)
# print('z' in nome)
# print(20 * '-')
# print('á' not in nome)
# print('z' not in nome)


nome = input('Digite seu nome: ')
encontrar = input('Digite o que você quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')