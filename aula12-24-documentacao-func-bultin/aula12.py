num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")

# num1 = int(num1)  # se tiver a conversão int(num1) erro em num1.isnumeric ou isdigit()
# num2 = int(num2)

print('é numero num1: ', num1.isdigit())
print('é numero num2: ', num2.isnumeric)

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(f'soma de {num1} com {num2} é ', num1 + num2)
else:
    print(f'não é int os numeros {num1} e {num2}')

print('Agora usando try e except no lugar de if else elif')
num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROU float')