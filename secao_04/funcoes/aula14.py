"""
Higher Order Functions - Funções de Ordem Superior(Funções de primeira classe)
Uma linguagem de programação é dita de primeira classe quando trata funções como qualquer outra variável.
"""

def saudacao(msg, nome):
    return f'{msg} tudo bem {nome}?'

def executa(funcao, *args):
    return funcao(*args)


var = executa(saudacao, 'Olá', 'João')

print(var)