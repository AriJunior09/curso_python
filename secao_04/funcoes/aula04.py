"""
Escopo de funções em Python
O escopo de uma variável determina onde ela pode ser acessada no código.
Variáveis definidas dentro de uma função são locais a essa função e não podem ser acessadas fora dela.
Variáveis definidas fora de qualquer função são globais e podem ser acessadas de qualquer lugar do código.
Variáveis globais podem ser acessadas dentro de funções, mas para modificar uma variável global dentro de uma função, é necessário usar a palavra-chave 'global'.

"""
y = 20          # Variável global

def escopo():
    x = 10      # Variável local
    print('Dentro da função, x =', x)
    print('Dentro da função, y =', y)  # Acessa a variável global

    def outra_funcao():
        z = 30  # Variável local à outra_funcao
        print('Dentro de outra_funcao, z =', z)
    outra_funcao()

print('Fora da função, y =', y)

escopo()
