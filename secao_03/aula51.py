"""
enumerate - enumera iteráveis (indices)"""

lista = ['Ari', 'Rute', 'Tiago']
lista.append('Caio')

lista_enumerada = list(enumerate(lista))

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)


for indice, nome in enumerate(lista):
    print(indice, nome)
