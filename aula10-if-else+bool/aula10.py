"""
aulas 20 a 22 por enquanto
IF, ELIF e ELSE - BOOL
cada inicio com if é um bloco a ser executado
"""
if True:
    print("verdadeiro")
elif False:
    print('test elfi')

if False:
    print("verdadeiro")
elif True:
    print('test elfi')
else:
    print("passou!")

if False:
    print("verdadeiro")
else:
    print("não é verdadeira")
print("Expressão não é verdadeira")

if True:
    print("true1")
elif True:
    print('true2')
elif True:
    print('true3')
elif True:
    print('true4')

if False:
    print("true1")
elif False:
    print('true2')
elif False:
    print('true3')
elif False:
    print('true4')
else:
    print('else no final')
idade_menor = 18
idade_limite = 33
print(f'idade menor é {idade_menor}')
print(f'idade maior é {idade_limite}')
nome = input("qual seu nome: ")
idade = int(input("digite sua idade: "))

if 'u' in nome:
    print(f'contem letra u em {nome}')
else:
    print('nao contem letra u')

if 'u' not in nome:
    print(f'invertido contem letra u em {nome}')
else:
    print('nao invertido para u')


if idade_menor == idade:
    print(f'a idade é igual a idade menor {idade_menor}')
else:
    print('diferente da idade menor')

# if idade >= idade_limite:
#     print(f'{nome} pode fazer o emprestimo')
# else:
#     print('nao pode fazer o emprestimo')

# if idade >= idade_menor and idade <= idade_limite:
#     print(f'{nome} pode fazer o emprestimo')
# else:
#     print('nao pode fazer o emprestimo')

if idade_menor <= idade <= idade_limite:
    print(f'{nome} pode fazer o emprestimo')
else:
    print('nao pode fazer o emprestimo')


if not idade_menor <= idade <= idade_limite:
    print(f'{nome} pode fazer o emprestimo invertido')
else:
    print('nao pode fazer o emprestimo nao invertido')

nome = 'Joãozinho'
idade = """40"""
peso = 80.5
e_maior = True
idade = int(idade)

if idade > 18:
    print(f'{nome} é maior de idade.')
else:
    print(f'{nome} NÃO é maior de idade.')

usuario = input('nome do usuario: ')
senha = input('senha do usuario: ')

usuario_db = 'pcorrea@test.com'
senha_db = '1234'

if usuario_db == usuario and senha_db == senha:
    print(f'usuario {usuario} está Ok com senha {senha}')
else:
    print(f'usuario {usuario} incorreto ou a senha {senha} incorreta tente outra vez')