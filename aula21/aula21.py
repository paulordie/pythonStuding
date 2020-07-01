# lista dentro de []

# append, insert, pop, del, clear,extend

paulo = ['paulo', 33, 'analista técnico']
string = 'Paulo'
print(f'string: {string[1]} agora a lista paulo o index 1: {paulo[0]} {paulo[2]}')
#         0   1   2   3   4
#        -5  -4  -3  -2  -1
lista = ['A','B','C','D','E']

print(f'pegar o contéudo no index -4 da lista: {lista[-4]}')
print(f'vai imprimir ate o index 2 {lista[0:3]} {lista[:3]}')
print(f'vai imprimir entre 1 e 3 {lista[1:4]}')
print(f'ultimo {lista[-1]}')
print(f'inicia do 2 {lista[2:]}')
print(f'pular de 2 em 2 {lista[::2]}')
print(f'inverter a lista {lista[::-1]}')
print(f'inverter a lista antes de -3 {lista[:-3:-1]}')

l1 = [1,2,3]
l2 = [4,5,6]

l1.extend(l2)
l1.extend('z')
l1.extend('test')
l1.extend([123,23])
print(f'before pop lista1 {l1} lista2 {l2}')
l1.pop()

print(f'after pop lista1 {l1} lista2 {l2}')
l2.append('test01')
l2.insert(0, 'Paulo')

print(f'lista1 {l1} lista2 {l2}')
del(l1[3:5])
print(f'Lista 1 sera retirado do index 3 e 4 {l1}')
del(l1[-1])
print(f'Imprimir o último da lista1 {l1}')
l3 = [1,20,3.4,-1, 53]
list1 = list(range(10))
list2 = list(range(2,10,2))

print(f'max {max(l3)} min {min(l3)}')
print(f'list1 {list1} list2 {list2}')

for value in list1:
    print(f'list1 {value}')

listType = ['Paulo', 33, 1.71, True]

for element in listType:
    print(f'Which type on {element} is {type(element)}')

test02 = 'umaPalabraComTest'
size = len(test02)
print(test02)

withoutTest = size - 4

print(f'test02 {withoutTest}')




