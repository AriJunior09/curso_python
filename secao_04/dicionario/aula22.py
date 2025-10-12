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

respostas_certas = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print('Opções:')
    for i, opcao in enumerate(pergunta['Opções'], start=1):
        print(f'{i}) {opcao}')
    resposta = input('\nResposta: ')
    
    if resposta == pergunta['Resposta']:
        print('Você acertou!✅')
        respostas_certas += 1
    else:
        print('Você errou!❌')
    print()
print(f'Você acertou {respostas_certas} de {len(perguntas)} perguntas.')
# # -------------------------------------------------------------
