"""
Métodos úteis dos dicionários em Python
len - Retorna o número de itens (pares chave-valor) no dicionário.
keys - Retorna uma visão (view) das chaves no dicionário.
values - Retorna uma visão (view) dos valores no dicionário.
items - Retorna uma visão (view) dos pares chave-valor no dicionário.
setdefault - Retorna o valor de uma chave se ela existir; caso contrário, insere a chave com um valor padrão.
copy - Retorna uma cópia rasa (shallow copy) do dicionário.
get - Retorna o valor de uma chave se ela existir; caso contrário, retorna um valor padrão (None se não for especificado).
pop - Remove a chave especificada e retorna o valor associado a ela.
popitem - Remove e retorna um par chave-valor arbitrário do dicionário.
clear - Remove todos os itens do dicionário.
update - Atualiza o dicionário com os pares chave-valor de outro dicionário ou de um iterável de pares chave-valor.
"""

pessoa = {
    'nome': 'Ari',
    'sobrenome': 'Junior',
    'idade': 33
}

# print(len(pessoa))          # Retorna o número de itens (pares chave-valor) no dicionário.
# print(pessoa.keys())        # Retorna uma visão (view) das chaves no dicionário.
# print(list(pessoa.keys()))  # Convertendo a visão das chaves para uma lista
# print(pessoa.values())      # Retorna uma visão (view) dos valores no dicionário.
# print(list(pessoa.values()))  # Convertendo a visão dos valores para uma lista
# print(pessoa.items())         # Retorna uma visão (view) dos pares chave-valor no dicionário.
# print(list(pessoa.items()))   # Convertendo a visão dos pares chave-valor para uma lista


# for chave in pessoa.keys():
#     print(chave)

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

print(pessoa['sobrenome'])        # Junior
print(pessoa.get('sobrenome'))    # Junior
print(pessoa.get('idade'))        # 33
print(pessoa.get('altura'))       # None
print(pessoa.get('altura', 1.75)) # 1.75 - se não existir a chave, retorna o valor padrão
pessoa.setdefault('Signo', "Leão") # Se a chave não existir, cria a chave com o valor padrão

print(pessoa)