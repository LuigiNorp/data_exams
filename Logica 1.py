casilla =[2,3,1,5,7,6,21,7,11,9,0,2]

casilla[11-1] = casilla[3-1]+casilla[11-1]
casilla[5-1] = casilla[1-1]+casilla[casilla[9-1]-1]

while casilla[5-1]!=casilla[10-1]:
    casilla[12-1] = casilla[12-1]*casilla[12-1]
    if casilla[5-1]==casilla[10-1]:
        casilla[8-1] = casilla[7-1]-casilla[5-1]
        casilla[6-1] = casilla[12-1]+casilla[8-1]
        print(casilla[6-1])

    casilla[12-1] = casilla[12-1]-2
    casilla[5-1] = casilla[5-1] + casilla[2-1]
    print(casilla[6-1])
    print('siguiente iteracion')

    # Respuesta: 6 6