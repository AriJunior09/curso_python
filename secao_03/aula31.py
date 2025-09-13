"""
Repetições:
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
Para parar o loop, digite no terminal: Ctrl + C -> KeyboardInterrupt
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

print('Fim')