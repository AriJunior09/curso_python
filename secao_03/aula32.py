"""
Repetições:
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
Para parar o loop, digite no terminal: Ctrl + C -> KeyboardInterrupt
"""

inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))


while inicio <= fim:
    print(inicio)
    inicio = inicio + 1

print('FIM')