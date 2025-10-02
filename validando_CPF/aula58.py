""" Replace """

# cpf_enviado = '746.824.890-70'\
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')

# print(cpf_enviado)
# -----------------------------------------------------

'''Expressão Regular'''
# import re
# entrada = input('Digite seu CPF: ')

# cpf_enviado = re.sub(
#     r'[^0-9]',
#     '',
#     entrada
# )
# print(cpf_enviado)
# -----------------------------------------------------

""" Verificando se todos os digitos são iguais """
import re
entrada = input('Digite seu CPF: ')

cpf_enviado = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_eh_sequencial = entrada == entrada[0] * len(entrada)
if entrada_eh_sequencial:
    print('Você enviou dados sequenciais')
    exit()
