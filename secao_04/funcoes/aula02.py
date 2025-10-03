""""
Argumentos nomeados e não nomeados
Argumentos nomeados são aqueles que você especifica o nome do parâmetro ao chamar a função.
Argumentos não nomeados são aqueles que você passa na ordem dos parâmetros definidos na função.
"""

def soma(x, y):
    print(f'x={x} e {y=} | x + y = {x + y}')

soma(2, 3)       # Argumentos não nomeados
soma(y=2, x=4)   # Argumentos nomeados
soma(2, y=6)     # Mistura de argumentos nomeados e não
# Se nomear um argumento, todos os seguintes também devem ser nomeados
# soma(x=2, 3)    # Erro
# soma(2, y=3, 4) # Erro
