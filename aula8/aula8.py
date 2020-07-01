"""
Exercício proposto
"""

nome = 'Paulo'
print(nome)
print(nome, type(nome))

idade = 33
altura = 1.71
e_maior = idade > 18
peso = 90
imc = peso / (altura ** 2)
ano_atual = 2020
nascimento = ano_atual - idade - 1

print(f'{nome} tem {idade} anos, e {altura} de altura e peso {peso}')
print(f'O IMC de {nome} é de {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')

print("Meu nome é 'Luiz Otávio', mas me chamam de 'Otávio Miranda'")
print('Acho "Legal ter dois nomes.')