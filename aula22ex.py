""""
Exercicio:
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e a idade forem digitados:
    Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Seu nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {ultima_letra}
Se nada for digitado em nome ou idade:
    Exiba:
    'Desculpe, você deixou um ou mais campos vazios'
"""
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
espacos = nome.count(' ')

if nome and idade:
    print('-' * 50)
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if espacos > 0:
        print(f'Seu nome contem {espacos} espaços')
    else:
        print('Seu nome não contem espaços')

    print(f'Seu nome tem {len(nome) - espacos} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    print('Desculpe, você deixou um ou mais campos vazios')
