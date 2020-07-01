# positivos [012345678] inicia da esquerda para direita a contagem
# negativos -[987654321] inicia da direita para esquerda a contagem

texto = "Python s2"
print(texto[2])

url = 'www.google.com.br/'
print(url[:-1])

nova_string = texto[2:6]  # mas nao pegar o valor do 6 ou ultimo
nova_string1 = texto[:6]  # mas nao inclui o 6 e é implicito o inicio 0
nova_string2 = texto[7:]  # ele vai do 7 e até o ultimo caracter implicitamente
nova_string3 = texto[:-2]  # ele vai do 7 e até o ultimo caracter implicitamente
nova_string4 = texto[0:6:2]  # ele vai do 0 ate o 6 pulando de 2 em 2
print('string', nova_string)
print('string1', nova_string1)
print('string2', nova_string2)
print('string3', nova_string3)
print('string4', nova_string4)

for letra in texto:
    print(f'{letra}')
