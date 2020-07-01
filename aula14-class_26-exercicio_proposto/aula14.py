print('Verificar se o dois numeros são pares ou impares')

num1 = input('Digite o primeiro numero: ')
num2 = input('Digite o segundo numero: ')

if num1.isdigit and num1.isnumeric:
    num1 = int(num1)
    num1Result = num1 % 2

    # if num1 % 2 == 0:
    #     pass

    if num1Result != 0:
        print(f'num1 {num1} é impar com resto: {num1Result}')
    else:
        print(f'num1 {num1} é par com resto: {num1Result}')
else:
    print(f'ERRO em {num1}')

if num2.isdigit:
    num2 = int(num2)
    num2Result = num2 % 2

    if num2Result != 0:
        print(f'num1 {num2} é impar com resto: {num2Result}')
    else:
        print(f'num1 {num2} é par com resto: {num2Result}')
else:
    print(f'ERRO em {num2}')

print('Comprimentar de acordo com o horário do dia')

horaDoDia = input('Digite a hora do dia: ')

if horaDoDia.isdigit:
    horaDoDia = int(horaDoDia)

    if horaDoDia >= 0 and horaDoDia < 12:
        print(f'São {horaDoDia} então BOM DIA')
    elif horaDoDia >= 12 and horaDoDia < 18:
        print(f'São {horaDoDia} então BOA TARDE')
    elif horaDoDia >= 18 and horaDoDia < 24:
        print(f'São {horaDoDia} então BOA NOITE')
    elif horaDoDia >= 24:
        print(f'erro na hora {horaDoDia}')
    else:
        print(f'Alguma coisa deu errado em {horaDoDia}')
else:
    print(f'ERRO em {horaDoDia}')

print('Verificar o tamanho nome len entre 4, 5 e 6')

nome = input('Digite seu nome: ')

sizeNome = len(nome)

if sizeNome <= 4:
    print(f' Seu nome é muito curto {nome} são "4" tem size: {sizeNome}')
elif sizeNome == 5 or sizeNome == 6:
    print(f'Seu nome {nome} é normal entre 5 e 6 tem size: {sizeNome}')
elif sizeNome > 6:
    print(f'Seu nome {nome} é muito maior que "6" tem size: {sizeNome}')
else:
    print('Talvez não seja letra verifique o que digitou')

