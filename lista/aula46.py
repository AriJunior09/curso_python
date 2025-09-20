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

lista_a = [1, 2, 3]
lista_b = ['A', 'B', 'C']
lista_c = lista_a + lista_b

lista_a.extend(lista_b) # Estende a lista_a adicionando os valores da lista_b
print(lista_a)