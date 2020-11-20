import math

def percent(closed):
    
#    x = 1.785714286
    count = 27
    
    total = 53
    restante = total - count
    x = 100/restante
    revision = closed
    #final = closed - count
    faltam = total - closed
    final = closed - count
    print('De 27 até 53')
    print(f'Feitos {final} e restão ainda {faltam}')
    result = final * x
    numTestCase = count + closed
    f = x * total 
    #print(f)
   # print(f'ultimo finalizado é {revision} e finalizado {result}%')

    if closed > count and closed <= total:
        #rest = closed - count
        resultPercent = final * x
       # resultPercent = resultPercent - x
        print(f'ultimo finalizado é {revision} e finalizado {resultPercent:.2f}%')
    else:
        print('Tem um número estranho tente novamente')
        print('/**************************/')
while True:
    

    inNumRev = input('Em qual você está: ')
    inNumRev = int(inNumRev)
    if inNumRev <= 53:
        percent(inNumRev)
            
        print('/**************************/')
    elif inNumRev == 'f':
        break
