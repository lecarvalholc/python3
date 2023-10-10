nome = 'Leda Carvalho'
altura = 1.57
peso = 65

imc = peso / (altura * altura)
print(nome, 'tem', altura, 'de altura, pesa', peso, 'kg e seu IMC é:', imc)

#f-strings - formatação de strings
linha1 = f'{nome} tem {altura:.2f} de altura, pesa {peso} kg e seu IMC é: {imc:.2f}'
print(linha1)