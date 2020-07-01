minha_string = 'o rato roeu o roupa do rei de roma.'
tamanho_string = len(minha_string)

c = 0
contagem = 0
letra = ''

while c < tamanho_string:
    conta = minha_string.count(minha_string[c])

    if contagem < conta and minha_string[c].strip():
        letra = minha_string[c]
        contagem = conta

    c += 1

print(letra, contagem)

minha_string1 = 'o rato roeu o roupa do rei de roma rrRRRRRrrr.'
tamanho_string1 = len(minha_string1)

c1 = 0
novaString1 = ''


def showString(count, size, nova, minha):
    while count < size:
        if minha[count] == 'r':
            nova = nova + minha[count].upper()
        else:
            nova = nova + minha[count]

        count += 1

    print(f'nova é {nova}')

showString(c1, tamanho_string1, novaString1, minha_string1)


string = 'texto'

c = 0

stringMontada = ''

while c < len(string):
    print(f'valor da string {string[c]}')
    stringMontada = stringMontada + string[c]
    c += 1

print(f'valor final fora do while {c} e string montada é {stringMontada}')