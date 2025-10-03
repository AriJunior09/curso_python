"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

# condicao = 10 > 30
# variavel = 'Verdade' if condicao else 'Mentira'

# print(variavel)
# -----------------------------------------------

digito = 9          # Se for maior que 9 então vira 0
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('Valor-01' if False else 'Valor-02' if False else 'Valor-03')