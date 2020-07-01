"""
Iniciar com letra, pode conter numeros, separar _, letras minúsculas
"""
nome = 'Paulo'
print(nome)
print(nome, type(nome))

idade = 33
altura = 1.71
e_maior = idade > 18
peso = 90
imc = peso / (altura ** 2)
print("nome:", nome)
print("idade", idade)
print("altura", altura)
print("maior de 18:", e_maior)
print(idade * altura)
print(nome, "tem:", idade, "anos de idade e seu imc é de:", imc)
print(f'{nome} tem {idade} anos de idade e seu imc é de: {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))
print('{i} tem {n} {n} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))
print('{2} {0} {0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))

ano_atual = 2020
nascimento = ano_atual - idade - 1
print(f'{nome} tem {idade} anos, e {altura} de altura e peso {peso}')
print(f'O IMC de {nome} é de {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')

print("Meu nome é 'Luiz Otávio', mas me chamam de 'Otávio Miranda'")
print('Acho "Legal ter dois nomes.')