""" for in com listas """

# lista = [1991, 1.75, True, 'Helena']

# for nome in lista:
#     print(nome, type(nome))
# --------------------------------------------

lista = ['Ari', 'Helena', 'Ezequiel', 'Rute']
lista.append('Caio')
lista.append('Rita')
lista.remove('Helena')
indice = 0
print('-' * 20)
print(lista)
for nome in lista:
    print( indice, nome)
    indice += 1

print('-' * 20)
