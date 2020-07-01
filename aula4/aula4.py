""""
Tipos de dados: string int float double bool
mesma lógica para as outras lingagens e o para separar casas decimais é usado o ponto
'.'
"""

print(type('paulo'))  #type vai me mostrar o tipo da variavel
print('paulo', type('paulo'))
print(10, type(10))
print(25.23, type(25.23))
print(11 == 11, type(11 == 11))
print('L' == 'L', type('L' == 'L'))
print('L' == 'l', type('L' == 'L'))
print(bool())  # nao é operação de validadcao
print(bool([]))  # nao é operação de validadcao

#converter a variavel
print('paulo',type('paulo'),bool('paulo'))
print('10',type('10'),type(int('10')))

#exercicio
print('Paulo Correa', type('Paulo Correa'))
print('33', type('33'))
print(1.71, type(1.171))
print(33 > 18, type(33 > 18))