"""
Como o for funciona por baixo dos panos:

Iterável -> str, range, etc 
Iterável (tem um metodo dentro dele chamado __iter__)
Interador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
inter -> me entregue seu iterador
Método é tudo que chama depois do ponto(uma ação dentro do objeto tipo: .lower .upper .strip)
"""
# for letra in texto:

texto = 'Luiz'   # iterável
iterador = iter(texto) # iterador, Mesma coisa de usar o .__iter__()

# print(next(iterador))     # Mesmo que usar .__next__()

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

''' Mesma coisa usando o for: '''
# for letra in texto:
#     print(letra)
