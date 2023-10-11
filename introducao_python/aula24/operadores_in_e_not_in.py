# Operadores in e not in
# Strings são iteráveis - pode navegar item por item
# 0 1 2 3 -- índices
# L e d a -- posso navegar no L, no e, no d e no a usando os indices
# -4 -3 -2 -1

nome = 'Leda'
print(nome[3])  #retorna letra a
print(nome[-1]) #retorna letra a
print(10 * '-') #linha tracejada (------)

print ('a' in nome)          #se 'a' está entre as letras do nome - True
print ('z' in nome)          #se 'z' está entre as letras do nome - False
print ('Led' in nome)        #se 'Led' está entre as letras do nome - True
print ('Led' not in nome)    #se 'Led' não está entre as letras do nome - False

print(10 * '-') #linha tracejada (------)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'"{encontrar}" não está em {nome}')
