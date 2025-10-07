"""
Escopo
"""


def funcao_01():
    print('Função 01')

    def funcao_02():
        print('Função 02')
    funcao_02()

    def funcao_03():
        print('Função 03')
    
        def funcao_04():
            print('Função 04')
        funcao_04()

        def funcao_05():
            print('Função 05')
        funcao_05()

    funcao_03()

funcao_01()

