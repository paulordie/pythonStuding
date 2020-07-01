contador = 1
acumulador = 1

while contador <= 10:
    print(f'contador é {contador} e o acumulador é {acumulador}')

    if contador > 5:
        break
    acumulador = acumulador + contador
    contador += 1
    if acumulador > 40:
        print('Final do acumulador quando maior que 40')

else:
    print('Final do acumulador')