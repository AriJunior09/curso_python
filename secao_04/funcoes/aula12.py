"""
Exercicio: Crie uma função que multiplique todos os argumentos não nomeados recebidos.
"""

def multiplicar(*args):
    total = 1
    for i in args:
        total *= i
    return total

numero = int(input("Quantos números você quer multiplicar? "))
valores = []
for n in range(numero):
    valores.append(int(input(f'Digite o {n + 1}º valor: ')))

total = multiplicar(*valores)

print(total)

