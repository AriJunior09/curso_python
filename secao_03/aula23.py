"""
Introdução ao Try / Except
try → tentar executar o código
except → ocorreu algum erro ao tentar executar
"""

numero_str = input('Digite um numero: ')

try:
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O Dobro de {numero_str} é {numero_float * 2:.2f}')

except:
    print('Isso não é um número!')


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O Dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Não tem apenas numeros')




