"""
Introdução ao try/except
try - tentar executar o código
except - ocorreu algum erro ao tentar executar
"""

#print(123)
#print(456)
#int('a') #não tem como converter 'a' para inteiro assim

#input SEMPRE vem como string, precisamos tratar
numero_str = input('Vou dobrar o número que você digitar: ')

#if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
#else:
#    print('Isso não é um número')

#O 'if' NÃO evita erros, só checa a lógica em código

try:
    print(f'STR: {numero_str}')
    numero_float = float(numero_str)
    print(f'FLOAT: {numero_float}')
    print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
except:
    print('Isso não é um número')