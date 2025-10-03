# Operadores Lógicos
# or
# Se qualquer uma das condições for verdadeira tudo será verdadeiro


# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '1234'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

print(False or False or False or 'abc')
print(bool('') or 10)

senha = input('Senha: ') or 'Sem senha'
print(senha)

