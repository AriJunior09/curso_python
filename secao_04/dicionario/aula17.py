""" Dicionários:
São estruturas de dados que armazenam pares de chave-valor.
Cada chave é única e é usada para acessar o valor associado a ela.
Exemplo de criação e uso de um dicionário:
Chaves podem ser consideradas como índices, mas ao invés de serem números inteiros sequenciais, podem ser: str, int, float, bool, tuplas (imútaveis).
O valor pode ser qualquer tipo de dado, inclusive outros dicionários.
Usamos chaves {} ou a função dict() para criar dicionários.
Imutáveis: str, int, float, bool, tuplas (tuplas só podem conter valores imútaveis).
Mutáveis: listas, dicionários, conjuntos.
"""

# Criando um dicionário vazio

# dicio = {}
# dicio2 = dict()
# print(type(dicio))   # <class 'dict'>
# print(type(dicio2))  # <class 'dict'>

# Criando um dicionário com dados iniciais
# pessoa = dict(nome='João', idade=30, altura=1.75, peso=70.5)
pessoa = {
    'nome': 'João',
    'sobrenome': 'Silva',
    'idade': 30,
    'altura': 1.75,
    'peso': 70.5,
    'ativo': True,
    'endereços': [
        {'Rua A, 123'}, 
        {'Avenida B, 456'}
    ],
    'contato': {
        'nome': 'Ari',
        'email': 'ari@gmail.com',
        'telefone': '1234-5678'
    }
}

# print(pessoa['nome'])        # João

for chave in pessoa:
    print(chave, pessoa[chave])