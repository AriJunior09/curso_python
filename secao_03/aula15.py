# Operadores Lógicos:
# and
# Todas as condições precisam ser verdadeira para ser verdadeiro

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(True and True and False, 'Testando')
print(bool('-1'))
print(True and 0 and True)