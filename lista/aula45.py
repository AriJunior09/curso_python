"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis:
    append - Adiciona um item no final
    insert - Adiciona um item no indice escolhido
    pop    - Remove do final ou do indice escolhido
    del    - Apaga um indice
    clear  - Limpa a lista
    extend - Estende a lista
    + -    - Concatena a lista
"""
lista = [10, 20, 30, 40]
lista.append('Luiz')

nome = lista.pop()  # Remove o último item

lista.append(123)   # Adiciona no final
del lista[-1]       # Deleta o último item
# lista.clear()     # Limpa a lista

lista.insert(0, 'Ari')  # Adiciona o indice 0
print(lista)