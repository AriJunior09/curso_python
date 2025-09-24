""" Tipo tupla - Uma lista imutável"""


nomes = 'Ari', 'Rute', 'Ezequiel' # Tupla
nomes = list(nomes)               # Convertendo para lista
nomes[0] = 'Caio'                 # Mudando valor index 0
nomes = tuple(nomes)              # Convertendo para tupla
print(nomes, type(nomes))