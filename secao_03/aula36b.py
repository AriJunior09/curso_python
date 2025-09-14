while True:
    primeiro_numero = input('Digite o primeiro numero: ')
    segundo_numero = input('Digite o segundo numero: ')
    operacao = input('Qual a operação deseja fazer? ( + - * / ): ')
    numeros_validos = None
    try:
        n1 = float(primeiro_numero)
        n2= float(segundo_numero)
        numeros_validos = True

    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos!')
        continue

    operadores_permitidos = '+-*/'

    if operacao not in operadores_permitidos:
        print('Operação não permitida!')
        continue

    if len(operacao) > 1:
        print('Digite apenas um operador.')
    
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

        sair = input('Quer sair? [s]im: ').lower().startswith('s')

        if sair is True:
            break
    except:
        print('Operação não permitida')