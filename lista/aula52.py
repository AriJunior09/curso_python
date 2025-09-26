"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, 
apagar e listar valores da sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista.
"""

lista = ['ari', 'arroz', 'feijao']

while True:
    try:
        print('Selecione uma opção: ')
        opcao = input('[i]nserir [a]apagar [l]istar [s]air:')

        if opcao in 'iI':
            inserir = input('Digite o que deseja inserir: ')
            lista.append(inserir)

        elif opcao in 'aA':
            apagar = input('Digite o que deseja apagar: ')
            if apagar.isalpha:
                lista.remove(apagar)
            elif apagar.isdigit:
                apagar_int = int(apagar)
                lista.pop(apagar_int)

        elif opcao in 'lL':
            for i in lista:
                print(lista.index(i), i.capitalize())

        elif opcao in 'sS':
            print('Saindo...')
            break
    except:
        print('\nVamos tentar novamente!')
        continue


    # sair = input('Quer sair? [s]im / [n]ão: ').lower().startswith('s')

    # if sair is True:
    #     print('Saindo...')
    #     break        