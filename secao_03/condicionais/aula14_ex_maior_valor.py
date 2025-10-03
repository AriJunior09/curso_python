# Usuario digita dois valores e o sistema diz qual valor é maior


primeiro = input("Digite o primeiro valor: ")
segundo = input("Digite o segundo valor: ")

if  primeiro > segundo:
    print('O primeiro é maior')

elif segundo > primeiro:
    print('O segundo valor é maior')

else:
    print('Os números são iguais')