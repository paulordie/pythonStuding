"""
formatando valores

string = > :s
inteiros => :d
numero ponto flutuante = > :f
quantidade de casas decimais em ponto flutuante (:.(numero)f
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
"""


num_1 = 10
num_2 = 3
num_11 = 1
num_12 = 1150
divisao = num_1 / num_2
print('{}'.format(divisao))
print('{:.2f}'.format(divisao))
nome = 'Paulo Correa'
sobrenome = 'Rocha'
qualquer = 'anything'
nome_formatado = '{:@>15}'.format(nome)  #maximo é 15 caracteres com variavel nome
# nome_formatado1 = '{n}{n}{n}{n}'.format(n = nome)  #maximo é 15 caracteres com variavel nome
nome_formatado1 = '{n:0<20}'.format(n = nome)  #maximo é 15 caracteres com variavel nome
nome_formatado2 = '{0:$^20} {1:#^100}'.format(nome, sobrenome)  #maximo é 15 caracteres com variavel nome
print(nome_formatado)
print(nome_formatado1)
print(nome_formatado2)
print(f'{nome:s}')  # nao formata nada
print(f'{nome:#^50}')

print(f' test1 {num_11:0>10}')
print(f' test -- {num_12:0>10}')
print(f'{num_12:0>10.2f}')

print(f'{num_11:0<10}')
print(f'{num_12:0<10}')

nome1 = 'Paul Correa'
nome1 = nome1.ljust(100, '#')
print(f'Formatado built-in {nome1}')
print(nome1.lower())
print(nome1.upper())

