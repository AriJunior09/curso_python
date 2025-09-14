"""" Interando strings com while """
#.......0123456789 (indices positivos)
nome = 'Ari Junior'  # Strings são iteraveis
#.....-10987654321 (indices negativos)

indice = 0
nova_string = ''

while indice < len(nome):
    letra = nome[indice]
    nova_string += f'*{letra}'
    indice += 1

nova_string += '*'
print(nova_string)


