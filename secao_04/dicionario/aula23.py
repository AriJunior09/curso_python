""" 
Sets são mutáveis, não aceitam valores duplicados e não possuem ordem.
Usar listas para opções de múltipla escolha quando a ordem importa.
Usar sets para opções de múltipla escolha quando a ordem não importa.

"""
# s1 = set() # set vazio
# s2 = set('Luiz') # set com elementos únicos de uma string
# print(s2) # Não mantém a ordem e não tem elementos duplicados
# s3 = set(['Luiz', 'Maria', 'João']) # set com elementos únicos de uma lista
# print(s3) # Não mantém a ordem e não tem elementos duplicados
# s4 = {'Camila'}     # set com um elemento
# print(s4, type(s4)) # set com um elemento

'''-------------------------------------------------------------'''
# Sets são eficientes para remover valores duplicados de uma lista

# lista = [1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5]
# s5 = set(lista)         # Remove valores duplicados
# print(s5, type(s5))     # {1, 2, 3, 4, 5} <class 'set'>
# lista = list(s5)        # Converte de volta para lista
# print(lista)            # [1, 2, 3, 4, 5]


s1 = {1, 2, 3}
print(s1)
s1.add(4)      # Adiciona um elemento
s1.add(4)      # Não adiciona duplicatas
s1.discard(3)  # Remove um elemento (sem erro se o elemento não existir)
print(s1)

print(2 in s1) # Verifica se o elemento existe no set
print(len(s1)) # Tamanho do set

for numero in s1:
    print(numero)