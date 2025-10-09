# Manipulando chaves e valores em dicionários

pessoa = {}     # Criando um dicionário vazio

chave = 'nome'        # Criando uma variável chave
pessoa[chave] = 'Ari' # Add uma nova chave-valor ao dicionário
pessoa['sobrenome'] = 'Junior' # Add uma nova chave-valor ao dicionário

print(pessoa)         # {'nome': 'Ari', 'sobrenome': 'Junior'}

print(pessoa['nome']) # Acessando -> Ari
print(pessoa['sobrenome'])  # Acessando -> Junior

pessoa['sobrenome'] = 'Alves' # Atualizando o valor de uma chave existente
print(pessoa)         # {'nome': 'Ari', 'sobrenome': 'Alves'}


del pessoa['sobrenome'] # Deletando uma chave-valor do dicionário
print(pessoa)         # {'nome': 'Ari'}

if pessoa.get('sobrenome') is None: # Verificando se a chave existe
    print('Chave "sobrenome" não existe') 
else:
    print(pessoa['sobrenome']) 
# Acessando o valor de uma chave que não existe sem gerar erro