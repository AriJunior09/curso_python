"""
for + range
range -> range(star, stop, step)
(começo, fim, salto)
"""
numeros_1 = range(12)         # Números de 0 a 11
numeros_2 = range(3, 15)      # Números de 3 a 14
numeros_3 = range(4, 20, 2)   # Números de 4 a 18 pulando de 2 em 2
numeros_4 = range(0,-100,-10) # Números de 0 a -90 pulando de 10 em 10


for numero in numeros_1: 
    print(numero)

print('-' * 20)

for numero in numeros_2:
    print(numero)

print('-' * 20)

for numero in numeros_3:
    print(numero)

print('-' * 20)

for numero in numeros_4:
    print(numero)

