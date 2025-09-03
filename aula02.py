# Entendendo o print

# print() -> função que imprime uma mensagem na tela
# print(valor1, valor2, ..., sep=' ', end='\n')
# sep -> separador entre os valores, padrão é espaço
# end -> o que é colocado no final da impressão, padrão é nova linha (\n)


# \r e \n -> CRLF
# \n -> LF
# \r -> CR
# Siginifica "carriage return" e "new line"
# São caracteres especiais que indicam retorno de carro e nova linha, respectivamente.
# O que faz o \n?
# Ele move o cursor para a próxima linha.
# O que faz o \r?
# Ele move o cursor para o início da linha atual.

print(1, 2, 3)
print(1, 2, 3, sep='-', end=' FIM\n')
print(1, 2, 3, sep='-', end=' FIM\r\n')
print(type(123))
print(type("asc"))
print(type(True))
print('teste "caio" aqui')
