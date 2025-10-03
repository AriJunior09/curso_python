"""
Valores padrão para parâmetros
Ao definir uma função, você pode atribuir valores padrão aos parâmetros.
Caso o valor não seja fornecido na chamada da função, o valor padrão será usado.
Isso torna os parâmetros opcionais e pode simplificar chamadas de função.
Refatorar: editar o código para melhorar sua estrutura sem alterar seu comportamento externo.

"""

def soma(x, y, z=None):  # z tem valor padrão None
    if z is None:
        print(f'x={x}, y={y} | x + y = {x + y}')
    else:
        print(f'x={x}, y={y}, z={z} | x + y + z = {x + y + z}')
    

soma(2, 3)        # z assume o valor padrão None
soma(2, 3, 4)     # z recebe o valor 4
