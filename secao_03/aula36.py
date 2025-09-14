""" Calculadora com while """

primeiro_numero = input('Digite o primeiro numero: ')
operacao = input('Qual a operação deseja fazer? ( + - * / ): ')
segundo_numero = input('Digite o segundo numero: ')

try:
    n1 = int(primeiro_numero)
    n2= int(segundo_numero)

    if primeiro_numero.isdigit():
        if segundo_numero.isdigit():
            try:
                if operacao == '+':
                    resultado = n1 + n2
                    print(f'A soma de {n1} + {n2} é = {resultado}')

                elif operacao == '-':
                    resultado = n1 - n2
                    print(f'A subtração de {n1} - {n2} é = {resultado}')

                elif operacao == '*':
                    resultado = n1 * n2
                    print(f'A multiplicação de {n1} * {n2} é = {resultado}')

                elif operacao == '/':
                    resultado = n1 / n2
                    print(f'A divisão de {n1} / {n2} é = {resultado}')
            except:
                print('Erro na operação, não pode dividir por zero!')
except:
    print('\nDigite apenas numeros!')
