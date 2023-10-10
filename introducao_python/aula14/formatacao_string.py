a = 'A'
b = 'B'
c = 1.1

formato = 'a= {}, b= {} c= {:.2f}'.format(a, b, c)

string = 'a= {}, b= {}, c= {}'
formato2 = string.format(a, b, c)

print(formato)
print(formato2)

string = 'b= {1}, a= {0}, c= {2}'
formato3 = string.format(a, b, c)
print(formato3)

string = 'c= {nome3}, a= {nome1}, b= {nome2}'
formato4 = string.format(nome1=a, nome2=b, nome3=c)
print(formato4)