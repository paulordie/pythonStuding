"""
Split, Join, enumerate
"""

string = "O Brasil é o país do futebol, o Brasil é penta né Brasil"

lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0


#for valor in lista_1:
for valor in lista_1:
    #print(valor)
    #print(f' A palavra "{valor}" ocorreu: {lista_1.count(valor)}')
    qtd_vezes = lista_1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que ocorreu mais vezes é {palavra} com {contagem}x')
print('\n')

palavra1 = ''
contagem1 = 0


#for valor in lista_1:
for valor in lista_2:
    print(valor.strip().capitalize())

print('\n')
#lista = ['O','Brasil','é','Penta']
string = 'O Brasil é Penta.'
lista = string.split(' ')
string2 = '))))))'.join(lista)
print(string)
print(lista)
print(string2)

print('\n')

string1 = 'O Brasil é Penta.'
lista1 = string.split(' ')

for indice, valor in enumerate(lista1): #enumerate retorna tuplas
    print(indice, valor)
    print(f'item lista é: {lista1[indice]}')


lista2 = [
    [1,2],
    [3,4],
    [5,6]
]

for v in lista2:
    print(f'coluna 0: {v[0]} coluna 1: {v[1]}')
print('\n')

lista3 = [
    [0, 'Paulo'],
    [1, 'Giselle'],
    [2, 'Paola']
]

for indice, nome in lista3:
    print(f'indice é {indice} e nome: {nome}')
print('\n')
lista4 = [ 'Paulo', 'Giselle', 'Paola']

for indice, nome in enumerate(lista3): #desempacotamento
    print(f'indice é {indice} e nome: {nome}')
print('\n')
lista5 = [ 'Paulo', 'Giselle', 'Paola']
n1, n2, n3 = lista5 #desempacotamento
print(f'mostar n3: {n3}')