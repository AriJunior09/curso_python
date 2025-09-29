"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
MAIS O PRIMEIRO DIGITO
multiplicando cada um dos valores por uma
contagem regressiva començando de 11

EX: CPF: 746.824.890-70
  11 10  9  8  7  6  5  4  3  2
   7  4  6  8  2  4  8  9  0  7
  77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14= 363
Multiplicar o resultado anterior po 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado será 0
contrario disso:
    resultado é o valor da conta.
Nesse caso o SEGUNDO dígito do CPF é 0

"""
cpf = '74682489070'
dez_digitos = cpf[:10]
contador_regressivo_2 = 11
resultado_dig_2 = 0

for digito_2 in dez_digitos:
    resultado_dig_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_dig_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)
