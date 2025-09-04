# Aprendendo condições
# if, elif, else
# Condições simples e compostas

idade = 33
maior_idade = 18

# Condição simples
if idade >= maior_idade: print('É maior de idade')


# # Condição simples com bloco
if idade >= maior_idade:
    print('É maior de idade')
else:
    print('É menor de idade')


# # Condição composta
if idade < maior_idade:
    print('É menor de idade')
elif idade == maior_idade:
    print('Acabou de se tornar maior de idade')
elif idade:
    pass
else:
    print('É maior de idade')


# # Operador Ternário
print('É maior de idade') if idade >= maior_idade else print('É menor de idade')


# # Condição aninhada
if idade < maior_idade:
    print('É menor de idade')
    if idade == 17:
        print('Está quase se tornando maior de idade')
    else:
        print('Ainda falta um tempo para se tornar maior de idade')
else:
    print('É maior de idade')
    if idade == maior_idade:
        print('Acabou de se tornar maior de idade')
    else:
        print('Já é maior de idade há algum tempo') 
        if idade >= 65:
            print('É idoso')
        else:
            print('Ainda não é idoso')
# Fim

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Condição 1 é verdadeira')
elif condicao2:
    print('Condição 2 é verdadeira')
elif condicao3:
    print('Condição 3 é verdadeira')
elif condicao4:
    print('Essa condição não será executada, pois a condição 3 já é verdadeira')
else:
    print('Nenhuma condição é verdadeira')

print('Fim do programa')