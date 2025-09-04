# Aprendendo condições
# if, elif, else
# Condições simples e compostas

idade = 18
maior_idade = 18

# Condição simples
if idade >= 18: print('É maior de idade')


# Condição simples com bloco
if idade >= maior_idade:
    print('É maior de idade')
else:
    print('É menor de idade')


# Condição composta
if idade < 18:
    print('É menor de idade')
elif idade == 18:
    print('Acabou de se tornar maior de idade')
else:
    print('É maior de idade')


# Operador Ternário
print('É maior de idade') if idade >= 18 else print('É menor de idade')


# Condição aninhada
if idade < 18:
    print('É menor de idade')
    if idade == 17:
        print('Está quase se tornando maior de idade')
    else:
        print('Ainda falta um tempo para se tornar maior de idade')
else:
    print('É maior de idade')
    if idade == 18:
        print('Acabou de se tornar maior de idade')
    else:
        print('Já é maior de idade há algum tempo') 
        if idade >= 65:
            print('É idoso')
        else:
            print('Ainda não é idoso')
# Fim