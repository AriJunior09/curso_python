"""
Interpolação básica de strings
%s - string
%d e %i - int
%f - float
%x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
# variavel = 'Luiz, o preço é R$ 1000.95'
variavel = '%s, o preço é R$ %.2f'% (nome, preco)
print(variavel)

print('O hexadecimal de %d é %04x' % (5000965, 5000965))
print(f'{nome} o preço é R$ {preco:.2f}')