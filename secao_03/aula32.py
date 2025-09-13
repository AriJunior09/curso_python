"""
Repetições:
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
break -> interrumpe o while
continue - >
"""

contador = 0

while contador <= 20:
    contador += 1

    if contador >= 10 and contador <= 15:
        print('Não vou mostrar o ', contador)
        continue

    if contador == 19:
        print(contador,'Parei no 19 usando o break')
        break

    print(contador)

print('-' * 10,'FIM','-' * 10)


