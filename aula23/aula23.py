"""
For / Else
"""
test = True
for test in range(10):
    print('test1')
    continue
    print('test2')
    break

variavel = ['Paulo Correa','Giselle','Mel']

for valor in variavel:
    print(f'valores {valor}')
    print('\n')
    continue
    #break // vai sair da interação e o continue vai pular o proximo print
    print(valor)
    print('\n')


variavel1 = ['Paulo Correa','Giselle','Mel']

for valor in variavel1:
    if valor.startswith('G'):
        print('começa com G', valor)

    else:
        print('Não começa com G', valor)
print('\n')

variavel2 = ['Paulo Correa','Giselle','Mel']
comeca_com_g = False

for valor in variavel2:
    if valor.lower().startswith('g'):  # checka se é upcase ou lowcase a letra
        comeca_com_g = True

if comeca_com_g:
    print('Existe uma palavra que começa com G')
else:
    print('Não começa com G')


print('\n')
variavel3 = ['Paulo Correa','Giselle','Mel']

# for valor in variavel3:
#     if valor.lower().startswith('g'):
#         print(f'no for existe a palavra {valor}')
#         break
# else:
#     print('Não existe palavras com g ou G')

for valor in variavel3:
    if valor.lower().startswith('g'):
        print(f'no for existe a palavra e é {valor}')
        continue
    print(valor)