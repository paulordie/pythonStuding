'''
quantidade de caracteres
'''

usuario = input('Digite seu usuario: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('voce precisa de 6 caracteres')
else:
    print('vc foi cadastrado')

string1 = input('Digite string1: ')
string2 = input('Digite string2: ')

print(f'Quantidade de catacteres digitada nas duas strings é '
      f' {len(string1) + len(string2)}')
print(string2.__len__())  # nao conta float e int ou boolean
