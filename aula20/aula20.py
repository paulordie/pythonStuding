"""
For em python
função range(start,stop,step)
"""

texto = 'texto em Python'

for letraIdex in texto:
    print(f'a letra index é {letraIdex}')

for n, letra in enumerate(texto):
    print(f'n: {n} e letra {letra}')

for numero in range(10):
    print(f'sequencia de 0 a 9  {numero}')

for number in range(5, 20, 1):
    print(f'start em 4 até 20 pulando 1 {number}')

for number in range(5, 20, 2):
    print(f'start em 4 até 20 pulando 2 {number}')

for number in range(20, 10, -1):
    print(f'decrementa em -1 de 20 até 11 {number}')

for n in range(0, 100, 8):
    print(f'multiplo de 8 {n}')

for n in range(100):
    if n % 8 == 0:
        print(f'em if multiplo de 8 {n}')


texto1 = 'python'
novoTexto = ''

for letra in texto1:
    if letra == 't':
        novoTexto = novoTexto + letra.upper()
    elif letra == 'h':
        novoTexto += letra.upper()
    elif letra == 'n':
        continue
        novoTexto += letra
    else:
        novoTexto += letra
print(f'vai imprimir nova palavra {novoTexto}')

# continua - pula para o próximo laço
# braek termina o laço
