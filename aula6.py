# Conversão de tipos, coerção
# Type convertion, typecasting, coercion
# É o ato de converter o tipo em outro
#     Tipos imutáveis e primitivos:
# str, int, float, bool

print(1+1)
#print('1' + 1) - vai dar erro: str + inteiro
print('a' + 'b')
print(int('1'), type(int('1'))) #- fazer coerção
print(int('1') + 1)
print(float('1') + 1)
print(type(float('1') + 1))

#Qualquer coisa dentro do bool() é True
print(bool('1')) 
print(bool('3')) 
print(bool('5')) 
#Nada dentro do bool() é False
print(bool(''))

#Converter 11 para str - 11b
print(str(11) + 'b')