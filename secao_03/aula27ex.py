""" Faça um programa que peça ao usuário para digitar um número inteiro e informe se esse número é par ou impar.
Caso o usuário não tenha digitado um número inteiro, informe que não é um número inteiro.
"""



# Peça ao usuário para digitar um número inteiro
numero = input('Digite um número inteiro: ')

#Informe se esse número é par ou impar
try:
    numero_int = int(numero)
    if numero_int % 2 == 0 and type(numero_int) == int:
        print('Esse número é par!')
    else:
        print('Esse número é impar')
except:
    print('Isso não é um número inteiro!')
