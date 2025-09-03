# Exercicio 1: Crie uma Calculadora de IMC (Índice de Massa Corporal)
# Fórmula: IMC = peso / (altura ** 2)
""" O programa deve solicitar ao usuário que insira seu peso e altura
e exibir o resultado com uma mensagem apropriada.
Exemplo de saída:
>>> Seu IMC é 22.86, você está na faixa de peso normal. <<<
Dicas:
Use a função input() para obter dados do usuário.
Converta os valores de entrada para float.
Use a função round() para arredondar o resultado do IMC para duas casas decimais.
Classifique o IMC em categorias:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 24.9: Peso normal
- Entre 25 e 29.9: Sobrepeso
- 30 ou mais: Obesidade   """

# Solicita ao usuário que insira seu peso em kg
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
imc = round(imc, 2)  # Arredonda o IMC para duas casas decimais
print(f'{nome},', end=' ')
print(f'Seu IMC é {imc}.', end=' ')
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc <= 24.9:
    print("Você está na faixa de peso normal.")
elif 25 <= imc <= 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.") 

# Fim do código
