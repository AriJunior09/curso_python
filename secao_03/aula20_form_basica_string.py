# Formatação básica de strings
"""
s - string
d - int
s - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caracteres)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'AB'
print(variavel)
print(f'{variavel:->10}')
print(f'{variavel:-<10}')
print(f'{variavel:-^10}')
print(f'{1000.483256254632156:>.2f}')

print(f'O hexadecimal de 5800 é {5800:08X}')

