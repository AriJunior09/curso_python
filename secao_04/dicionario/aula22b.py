""" Exercício com Dicionários - Métodos úteis
get, pop, popitem, update, copy, deepcopy"""

perguntas = [
    {
        'Pergunta': 'Quanto é 3 * 10 ?',
        'Opções': ['10', '30', '40', '50'],
        'Resposta': '30'
    },
    {
        'Pergunta': 'Quanto é 5 * 12 ?',
        'Opções': ['50', '58', '60', '75'],
        'Resposta': '60'
    },
    {
        'Pergunta': 'Quanto é 10 / 2 ?',
        'Opções': ['4', '5', '2', '10'],
        'Resposta': '5'
    }
]
quantidade_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])

    for i, opcao in enumerate(pergunta['Opções'], start=1):
        print(f'{i}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')

    escolha_int = None
    if escolha.isdigit():
        escolha_int = int(escolha)
    if escolha_int is not None and 1 <= escolha_int <= len(pergunta['Opções']):
        if pergunta['Opções'][escolha_int - 1] == pergunta['Resposta']:
            print('Você acertou!✅\n')
            quantidade_acertos += 1
        else:
            print('Você errou!❌\n')
    else:
        print('Digite uma opção válida!')
    

print('Você acertou {} de {} perguntas.'.format(quantidade_acertos, len(perguntas)))
