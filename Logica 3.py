casilla = [8, 6, 5, 7, 3, 2, 2, 11, 10, -2, 4, 1]

casilla[11-1] = 1 + casilla[11-1]
casilla[10-1] = casilla[1-1]
if casilla[1-1]%2 != 0:
    casilla[10-1] = casilla[1-1]
    print(casilla[8-1])
    print(casilla[1-1])
    exit()
else:
    casilla[10-1] = 2 + casilla[1-1]
    casilla[11-1] = casilla[5-1] + casilla[11-1]
    casilla[10-1] = casilla[10-1] - (casilla[1-1] + casilla[12-1])
    if casilla[10-1] < casilla[1-1]:
        print(casilla[8-1])
        print(casilla[1-1])
        exit()
    else:
        casilla[10-1] = casilla[1-1]
        print(casilla[8-1])
        print(casilla[1-1])
        exit()