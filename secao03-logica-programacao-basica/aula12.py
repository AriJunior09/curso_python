# Aprendendo condições

entrada = input('Você quer "entrar" ou "sair"?: ').lower()


if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Digite uma opção válida!')