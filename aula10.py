# Entendendo format
# Formatação de strings

a = 'A'
b = 'B'
c = 1.123456789
string = 'a= {}, b= {}, c= {:.2f}'.format(a, b, c) # Usando ordem

print(string)


string_02 = 'a= {1}, b= {0}, c= {2:.3f}'.format(a, b, c) #Usando índices
print(string_02)    

string_03 = 'a= {x}, b= {y}, c= {z:.4f}'.format(x=a, y=b, z=c) #Usando parâmetros nomeados
print(string_03)