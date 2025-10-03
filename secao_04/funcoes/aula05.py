""" Funções dentro de funções - Aula 05
Funções podem ser definidas dentro de outras funções.
Isso é útil para organizar o código e criar funções auxiliares que não precisam ser acessíveis fora da função principal.
Essas funções internas podem acessar variáveis do escopo da função externa.
"""

x = 1

def escopo():
    x = 10     # Variável local

    def outra_funcao():
        y = 2
        print(x, y)  # Acessa a variável local x=10 e y=2
    outra_funcao()   # Chama a função interna x=10 e y=2
    
    print(x)         # Acessa a variável local x=10

escopo()             # Chama a função externa x=10
print(x)             # Acessa a variável global x=1
