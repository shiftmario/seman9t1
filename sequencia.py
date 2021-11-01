def sequencia():
    cont = 0
    numero = 0
    seque = []
    while cont < 100:
        numero = numero + 10
        seque.append(numero)
        cont += 1

    
    print(*seque, sep = ', ')

sequencia()