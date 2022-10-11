casilla = [-8, 13, 1, 6, 2, 5, 13, 6, 4, 7, 5, 2, 6, 7, 9]

casilla[1-1] = casilla[4-1] - casilla[casilla[7-1]-1]
while True:
    casilla[1-1] =  casilla[1-1] + casilla[6-1]
    if casilla[1-1]%4 == 0:
        continue
    casilla[1-1] = casilla[6-1] + casilla[11-1]

    if casilla[2-1] > casilla[6-1]:
        casilla[10-1] = casilla[10-1] - 2
        print(casilla[1-1])
        continue
    break

# Respuesta: 10 10 10 10 10...