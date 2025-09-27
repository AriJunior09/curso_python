"""
Lista de listas e seus indices
"""

salas = [
    #  0       1
    ['Ari', 'Rute'],            # 0
    #  0
    ['Yasmim'],                 # 1
    #  0        1         2     
    ['Enzo', 'Eduarda', 'Caio'] # 2
]

# print(salas[2][3][1])

for sala in salas:
    # print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
