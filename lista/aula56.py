"""
Desempacotando em chamadas de métodos e funções"""

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 4, 'Eduarda']
tupla = ('Python', 'é', 'legal')
salas = [
    #  0       1
    ['Ari', 'Rute'],            # 0
    #  0
    ['Yasmim'],                 # 1
    #  0        1         2     
    ['Enzo', 'Eduarda', 'Caio'] # 2
]

# prim, seg, *_, antepenutimo, ultimo = lista
# print(prim, _)

# for nome in lista:
#     print(nome, end= ' ')

print(*salas, sep='\n') 