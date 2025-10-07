""" 
Escopos
"""

x = 1  # Variável global

def escopo():
    x = 10  # Variável local

    def outra_funcao():
        y = x * 2  # Acessa a variável local x=10
        print(f'Outra função: x={x}, y={y}')  # Acessa x=10 e y=20
    

    outra_funcao()  # Chama a função interna
    print(f'Escopo: x={x}')  # Acessa a variável local x=10


