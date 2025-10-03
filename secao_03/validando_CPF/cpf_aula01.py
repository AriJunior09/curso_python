"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva començando de 10

EX: CPF: 746.824.890-70
  10  9  8  7  6  5  4  3  2
   7  4  6  8  2  4  8  9  0
  70 36 48 56 12 20 32 27  0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior po 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado será 0
contrario disso:
    resultado é o valor da conta.
Nesse caso o primeiro dígito do CPF é 7

"""
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
resultado_dig_1 = 0

for digito_1 in nove_digitos:
    resultado_dig_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_dig_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)
