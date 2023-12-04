"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs: a função len retorna a quantidade de 
caracteres da str
"""
#O ESPAÇO É UM CARACTER VÁLIDO

variavel = 'Olá mundo'
print(variavel[5])      #u
print(variavel[-4])     #u
print(variavel[4:])     #mundo - não tem indice final
print(variavel[4:8])    #mund - começa no m, até o 'o'
#indice final não é incluído
print(variavel[0:5])    #olá m
print(variavel[-8:5-2]) #lá

print(len(variavel))    #caractere != indice
print(len(variavel[3])) #quantidade de caractere
print(variavel[0:9:1])  #1 em 1 - Olá mundo
print(variavel[0:9:2])  #2 em 2 - Oámno
print(variavel[::-1])   #conttrário - odnum álO  