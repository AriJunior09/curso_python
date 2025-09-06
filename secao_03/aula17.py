# Operador Lógico
# not
# Inverte a expressão o que era True vira False e vice versa

senha = input('Senha: ')

if senha == '1234':
    print('Entrou')
else:
    print('Senha incorreta')

# #---------------------------------

if senha != '1234':
    print('Senha incorreta')

# #---------------------------------

if not senha:
    print('Você não digitou nada!')

print(not True)
print(not False)
print(not 1)