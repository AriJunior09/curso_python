def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

numero = int(input("Quantos números você quer somar? "))
valores = []
for n in range(numero):
    valores.append(int(input(f"Digite o {n + 1}º valor: ")))
print(soma(*valores))