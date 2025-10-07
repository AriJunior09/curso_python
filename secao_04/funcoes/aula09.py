"""
args - Argumentos não nomeados
kwargs - Argumentos nomeados
* - Desempacotamento de iteráveis
** - Desempacotamento de dicionários
*args (empacotamento de iteráveis)
**kwargs (empacotamento de dicionários)

"""

def soma(*args):
    total = 0
    for numero in args:
        print(f'{total} + {numero}')
        total += numero
        print(f'        = {total}')
        
    print(f'Total final: {total}')


soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

