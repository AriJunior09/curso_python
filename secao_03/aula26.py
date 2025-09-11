"""
Flag = (Bandeira) Marcar um local
None = Não valor
is   = É (tipo, valor, identidade)
is not = não é (tipo, valor, identidade)
id   = Identidade
"""

condicao = True
passou_no_if = None  # Exemplo de uma bandeira

if condicao:
    passou_no_if = True     
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if ->', passou_no_if)

if passou_no_if is not None: # Aqui podemos usar apenas um else
    print('Passou no if ->', passou_no_if)