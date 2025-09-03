# f-strings
# f  = formatted string (string formatada)
# Permite inserir expressões dentro de strings
# Utiliza chaves {} para inserir expressões
# Pode formatar números, datas, etc.


nome = "Ari"
idade = 33
altura = 1.75
peso = 84.5
imc = peso / (altura ** 2)

mensagem = f'{nome} tem {idade} anos e {altura:.2f} de altura.'
mensagem_02 = f'{peso} kg e seu IMC é {imc:.2f}.'

print(mensagem)
print(mensagem_02)