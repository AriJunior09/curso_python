""" 
Escopos
"""

x = 1  # Variável global

def escopo():
    x = 10  # Variável local
    print(f'x de dentro do escopo = {x}')  # Acessa a variável local x=10

    def outra_funcao():
        global x  # Declara que queremos usar a variável global x
        x = 100   # Modifica a variável global x
        y = x * 2
        print(f'y de dentro da outra_funcao = {y}')  # Acessa a variável local x=10

    outra_funcao()  

print(f'x na variável global antes de modificar = {x}')  # Acessa a variável global x=1
escopo()  # Chama a função externa x=10
print(f'x na variável global depois = {x}')  # Acessa a variável global x=1
