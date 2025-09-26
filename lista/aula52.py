"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, 
apagar e listar valores da sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista.
"""

import os
lista = []

while True:
    try:
        print('Selecione uma opção: ')
        opcao = input('[i]nserir [a]apagar [l]istar [s]air: ').strip().lower()

        if opcao in 'iI':
            os.system('cls')
            inserir = input('Digite o que deseja inserir: ')
            lista.append(inserir)

        elif opcao in 'aA':
            apagar = input('Digite o que deseja apagar: ')
            try:
                if apagar.isalpha():
                    lista.remove(apagar)

                if apagar.isdigit():
                    apagar_int = int(apagar)
                    del lista[apagar_int]
                print('Apagado!')

            except:
                print('Ops, não conseguimos apagar.')

        elif opcao in 'lL':
            os.system('cls')

            if len(lista) == 0:
                print('Nada para listar!')

            print('-' * 18)
            for i, valor in enumerate(lista):
                print(i, valor.capitalize())
            print('-' * 18)

        elif opcao in 'sS':
            print('Saindo...')
            break
    except:
        print('\nVamos tentar novamente!')
        continue


