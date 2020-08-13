import math

def percent(closed):
    x = 1.8182
    count = 57
    revision = closed
    resPerc = closed * x
    numTestCase = count + closed

    if count < closed and closed <= 113:
        rest = closed - count
        resultPercent = rest * x
       # resultPercent = resultPercent - x
        print(f'ultimo finalizado é {revision} e finalizado {resultPercent}%')

while True:
    inNumRev = input('Em qual você está: ')
    inNumRev = int(inNumRev)
    if inNumRev <= 113:
        percent(inNumRev)
            
    elif inNumRev == 'f':
        break
