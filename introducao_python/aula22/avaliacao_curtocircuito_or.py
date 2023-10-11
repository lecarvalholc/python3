# Operadores lógicos
# and (e) / or (ou) / not (não)
# and - Todas as condições precisam ser verdadeiras. Se qualquer valor da expressão 
# for considerado falso, a expressão inteira será avaliada naquele valor.
# São considerados falsy
# 0 / 0.0 / '' / False
# Também existe o tipo None que é usado para representar um não valor

# Avaliação de curto circuito
print(True or False)
print(0 or False or 0 or 'abc')
print(0 or False or 0 or 'abc' or True)

senha = input('Senha: ') or 'Sem senha'
print('Sua senha é:',senha)