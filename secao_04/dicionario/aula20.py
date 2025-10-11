""" Métodos Copy (Shallow Copy):
copy - Retorna uma cópia rasa (shallow copy) do dicionário.
Cria um novo objeto na memória, mas os objetos internos (valores) são referências aos mesmos objetos do dicionário original.
Atribuição (sinal de igual) - Não cria uma cópia, apenas uma referência ao mesmo objeto na memória.
deepcopy 
"""
# Use o deepcopy para uma cópia profunda onde copia até os valores mutáveis internos

import copy

dic_01 = {
    'nome': 'Ari',
    'sobrenome': 'Junior',
    'idade': 33,
    'lista': [0, 1, 2, 3]
}

dic_02 = dic_01 # Atribuição - Não cria uma cópia, apenas uma referência ao mesmo objeto na memória
dic_03 = dic_01.copy() # Cópia rasa (shallow copy) - Cria um novo objeto na memória
dic_04 = copy.deepcopy(dic_01)

dic_01['nome'] = 'Ariel' # Alterando o valor de uma chave existente
dic_01['lista'][3] = 999 #

print('Dic_01', dic_01) # dic_01 reflete a mudança
print('Dic_02', dic_02) # dic_02 é uma referência ao mesmo objeto que dic_01, então reflete as mudanças
print('Dic_03', dic_03) # dic_03 é uma cópia independente, então não reflete as mudanças feitas em dic_01
print('Dic_04', dic_04)

# Verificando os IDs (endereços na memória) dos dicionários
print(id(dic_01)) # ID de dic_01
print(id(dic_02)) # ID de dic_02 (mesmo que dic_01)
print(id(dic_03)) # ID de dic_03 (diferente de dic_01 e dic_02)
print(id(dic_04))
