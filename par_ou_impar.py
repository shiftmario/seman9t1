def impar_ou_par():
    n = par = impar = 0
    while n < 100:
        n += 1
        div = n % 2
        if div == 0:
            par += 1
        else:
            impar +=1

    print(f'Quantidade de números impares:{impar}')
    print(f'Quantidade de números pares:{par}')

impar_ou_par()