# Fatiamento de String
"""
012345678
Olá mundo
-987654321
Fatiamento [inicio:fim:passo] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'
# print(variavel[5])
# print(variavel[-4])

# print(variavel[4:])
# print(variavel[2:5])

# print(len(variavel[2:5]))
print(variavel[::-1])


# -----------------------------------------------------

concatenacao = 'Ari' + 'ado'
print(concatenacao)

repeticao = 'A' * 20
print(repeticao)

fatiamento = 'Ariado'[0:3]
print(fatiamento)

print('Ariado'[0])      # Primeiro caractere
print('Ariado'[-1])     # Último caractere
print('Ariado'[1:4])    # Do segundo ao quarto caractere


