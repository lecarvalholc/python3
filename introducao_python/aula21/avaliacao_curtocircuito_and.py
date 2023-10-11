# Operadores lógicos
# and (e) / or (ou) / not (não)
# and - Todas as condições precisam ser verdadeiras. Se qualquer valor da expressão 
# for considerado falso, a expressão inteira será avaliada naquele valor.
# São considerados falsy
# 0 / 0.0 / '' / False
# Também existe o tipo None que é usado para representar um não valor

# Avaliação de curto circuito
print(True and True and True)
print(True and False and True)
print(bool(0.0))
print(bool(0))
print(bool(''))