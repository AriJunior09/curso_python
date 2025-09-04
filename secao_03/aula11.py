# Usando a função input()
# Entrada de dados pelo usuário


nome = input('Qual é o seu nome? ') # A função input() sempre retorna uma string
print(f'Olá, {nome}')


x = input('Digite um número: ')
y = int(input('Digite outro número: '))

int_x = int(x) # Convertendo string para inteiro
int_y = int(y) # Convertendo string para inteiro

print(f'A soma é {int_x + int_y}') # Mostrando a soma dos números

