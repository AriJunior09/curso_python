"""
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro """

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

numero = int(input('Digite um número: '))

print(f'Duplo       = {duplicar(numero)}')      
print(f'Triplo      = {triplicar(numero)}')     
print(f'Quadruplo   = {quadruplicar(numero)}')   
