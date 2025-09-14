string = 'Qualquer valor'

i = 0

while i < len(string):

    letra = string[i]

    print(letra)
    i += 1

else:
    print('\nO else foi executado')
# Toda vez que o laço o while for até o final o else será executado
# Se usar o break no while o else não será executado


print('Fora do while')