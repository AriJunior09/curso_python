""" Funções - Aula 01
Intro: Funções são trechos de código que podem ser reutilizados várias vezes ao longo do código.
Elas podem receber entradas parâmetros (argumentos) e retornar saídas (valores).
Podem ajudar a organizar o código, torná-lo mais legível e facilitar a manutenção.
Por padrão, funções retornam None se não houver um return explícito.

"""

# def Print():
#     print('Eu')
#     print('Sou')
#     print('Ari')
#     print('Júnior')

# --------------------------------------------------------------
# def imprimir(a, b, c):       # a é o parâmetro
#     print(a, b, c)           # imprime os valores dos parâmetros


# imprimir(1, 2, 3)             # 1, 2 e 3 são os argumentos
# imprimir('Ari', 'é', 'oi')    # 'Ari', 'é' e 'oi' são argumentos
# imprimir('Ari', True, 1234)   # 'Ari', True e 1234 são argumentos
# --------------------------------------------------------------


def saudacao(nome):
    print(f'Olá {nome}, tudo bem?')

saudacao('Ariado')
saudacao('Maria')
saudacao('João')
saudacao('Ana')