lista = []

def listar():
    if not lista:
        print('Lista vazia.')
        return
    print('-' * 30)
    for idx, item in enumerate(lista):
        print(f'{idx} - {str(item).capitalize()}')
    print('-' * 30)

try:
    while True:
        print('Selecione uma opção:')
        opcao = input('[i]nserir [a]apagar [l]istar [s]air: ').strip().lower()

        if opcao == 'i':
            inserir = input('Digite o que deseja inserir: ').strip()
            if inserir:
                lista.append(inserir)
                print(f'Inserido: {inserir}')
            else:
                print('Nenhum valor inserido.')

        elif opcao == 'a':
            if not lista:
                print('Lista vazia. Nada a apagar.')
                continue

            apagar = input('Digite o item ou o índice a apagar: ').strip()

            # tenta converter para inteiro -> apagar por índice
            try:
                idx = int(apagar)
            except ValueError:
                # apagar por valor (primeira ocorrência)
                try:
                    lista.remove(apagar)
                    print(f'Item "{apagar}" removido.')
                except ValueError:
                    print(f'Item "{apagar}" não encontrado na lista.')
            else:
                # apagando por índice (verifica intervalo)
                if -len(lista) <= idx < len(lista):
                    removido = lista.pop(idx)
                    print(f'Item "{removido}" removido no índice {idx}.')
                else:
                    print('Índice fora do intervalo.')

        elif opcao == 'l':
            listar()

        elif opcao == 's':
            print('Saindo...')
            break

        else:
            print('Opção inválida.')

except KeyboardInterrupt:
    print('\nInterrompido pelo usuário. Saindo...')
