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