"""
Cuidados com os dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na meméria (mutável)
"""

# nome_a = 'Ari Júnior'
# nome_b = 'Ari Júnior'

# print(nome_a.isidentifier)
# print(nome_b.isidentifier)
# ------------------------------------------
# lista_a = [1, 2, 3]
# lista_b = lista_a

# lista_a[0] = 'Alterando lista_a' # Lista_b tambem será alterada
# print('Lista_a: ', lista_a)
# print('Lista_b: ', lista_b)
# ------------------------------------------
lista_a = [1, 2, 3]
lista_b = lista_a.copy()    # Lista_b terá uma copia

lista_a[0] = 'Alterando lista_a' # Lista_b não será alterada
print('Lista_a: ', lista_a)
print('Lista_b: ', lista_b)