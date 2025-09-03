# Tipo de dados no Python

# int -> números inteiros
# float -> números reais (com parte decimal)
# str -> cadeia de caracteres (texto)
# bool -> valores lógicos (True, False)
# O Python é uma linguagem de tipagem dinâmica
# Isso significa que não precisamos declarar o tipo da variável
# O Python infere o tipo da variável baseado no valor atribuído

# Exemplo:
idade = 25         # int
altura = 1.75      # float
nome = "João"      # str
estudante = True   # bool

print(idade , type(idade), sep='   ')
print(altura, type(altura))
print(nome, type(nome))
print(estudante, type(estudante))
print(type(10 == 10))

# Podemos converter entre tipos de dados
# int() -> converte para inteiro   
# str() -> converte para string
# float() -> converte para float
# bool() -> converte para booleano

a = "10"          # Tipo str
b = 2             # Tipo int
print("Converte a para int para somar: ", int(a) + b) # Converte a para int e soma com b

print("Converte b para string para concatenar: ", a + str(b)) # Converte b para str e concatena com a

c = float(a)      # Converte a para float
print("Converte a para float: ", c, type(c))
print(bool(" "))    # Qualquer string não vazia é True









