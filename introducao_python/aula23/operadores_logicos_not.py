# Operador lógico 'not'
# Usado para inverter expressões
# True = False
# False = True

senha = input('Senha: ')

if senha != '123456':
    print('Senha incorreta.')
if senha == '123456':
    print('Entrou.')
if not senha:
    print('Você não digitou a senha.')