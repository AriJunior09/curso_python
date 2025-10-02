"""
enumerate - enumera iteráveis (indices)"""

lista = ['Ari', 'Rute', 'Tiago']
lista.append('Caio')

lista_enumerada = list(enumerate(lista)) # transforma em lista
print(lista_enumerada)

for item in enumerate(lista):   # desempacotamento
    indice, nome = item         # desempacotamento
    print(indice, nome)         # acessando os valores

# Outra forma de fazer o mesmo

for indice, nome in enumerate(lista): # desempacotamento
    print(indice, nome)               # acessando os valores
