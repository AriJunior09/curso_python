""" args - Argumentos não nomeados """

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma1 = soma(1, 2, 3, 4, 5)
print(soma1)

soma2 = soma(10, 20, 3, 4, 5)
print(soma2)

print(sum((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
