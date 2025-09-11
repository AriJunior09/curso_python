""" Faça um programa que peça ao usuário para digitar um número inteiro e informe se esse número é par ou impar.
Caso o usuário não tenha digitado um número inteiro, informe que não é um número inteiro.
"""

# Peça ao usuário para digitar um número inteiro
numero = input('Digite um número inteiro: ')

#Verifique se foi digitado apenas numeros inteiros e Informe se esse número é par ou impar
try:
    if numero.isdigit():
        numero_int = int(numero)
        par_impar = numero_int % 2 == 0
        par_impar_texto = 'impar'
        
    if par_impar:
        par_impar_texto = 'par'
        
    print(f'O número {numero_int} é {par_impar_texto}')
    
except:
    print('Você não digitou um número inteiro!')
