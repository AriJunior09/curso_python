frase = 'O Python é uma linguagem de programação '\
        'multiparadigma. '\
        'Python foi criado por Guido Van Rossum'.lower()

# contar_letra = 'i'
# print(f'A letra {contar_letra} aparece: {frase.count(contar_letra.lower())} vezes')

i = 0
maior_qtd_aparicoes = 0
letra_mais_frequente = ''

while i < len(frase):
    letra = frase[i]

    if letra == ' ':
        i += 1
        continue

    qtd_aparicoes_letra_atual = frase.count(letra)

    if maior_qtd_aparicoes < qtd_aparicoes_letra_atual:
        maior_qtd_aparicoes = qtd_aparicoes_letra_atual
        letra_mais_frequente = letra
    i += 1

print('A letra que apareceu mais vezes foi ' \
f'"{letra_mais_frequente}" que apareceu '
f'{maior_qtd_aparicoes}')