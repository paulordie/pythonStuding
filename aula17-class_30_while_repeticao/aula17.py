while False:
    print('test')
    nome = input('Qual seu nome? ')
    print(f'Nome é {nome}')
print("Saiu do While")

x = 0
while x < 5:
    # if x == 3:
    #     x = x + 1
    #     continue
    if x == 3:
        x = x + 1
        break
    print(f'valor de X é: {x}')
    x = x + 1
print('acabou')

x = 0  # Coluna

while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1
    print(f'valor de X é: {x}')
    x += 1

print('acabou!!!')

while True:
    print('while')
    num_1 = input('Digite primeiro numero: ')
    operador = input('Digite o operador: ')
    num_2 = input('Digite segundo numero: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Voce precisa digitar um numero valido')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('operador invalido')
    sair = input("voce deseja sair [s]im uo [n]ão: ")
    if sair == 's':
        break
