"""
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
"""

pessoa = {
    'nome': 'Ari',
    'sobrenome': 'Junior',
    'idade': 33
}
# print(pessoa['cpf'])     # KeyError
# print(pessoa.get('cpf')) # Quando a chave não existe, retorna None
# print(pessoa.get('cpf', 'Não encontrado')) # Não encontrado

'''-------------------------------------------------------------
pop - Remove o item com a chave especificada e retorna o valor correspondente.'''
# remover = pessoa.pop('sobrenome') # Remove a chave e retorna o valor
# print(remover) # Junior
# print(pessoa)  # {'nome': 'Ari', 'idade': 33}

'''-------------------------------------------------------------
popitem - Remove e retorna o último item do dicionário.'''

# ultima_chave = pessoa.popitem()
# print(ultima_chave) # ('idade', 33)
# print(pessoa)       # {'nome': 'Ari', 'sobrenome': 'Junior'}

'''-------------------------------------------------------------
update - Atualiza o dicionário com os pares chave-valor de outro dicionário ou de um iterável de pares chave-valor.'''

# pessoa.update({'nome': 'Caio', 'idade': 20, 'altura': 1.70}) # Atualiza os valores das chaves existentes e adiciona novas chaves

# pessoa.update(nome='Alex', idade=34) # Forma alternativa

# print(pessoa) # {'nome': 'Caio', 'sobrenome': 'Junior', 'idade': 20, 'altura': 1.70}

# for chave, valor in pessoa.items():
#     print(f'{chave}: {valor}')

'''-------------------------------------------------------------'''
# Atualizando com uma lista de listas
lista = [ ['nome', 'Rafael'], ['sobrenome', 'Silva'], ['idade', 55] ]
pessoa.update(lista) # Atualiza o dicionário com uma lista de listas
print(pessoa) # {'nome': 'Rafael', 'sobrenome': 'Silva', 'idade': 55}