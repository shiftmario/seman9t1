def maior(valores):
    n = 1
    num = valores[0]
    while n < 100:
        if num < valores[n]:
            num = valores[n]
        
        n += 1
    print(f'O maior valor é:{num}')

numero = [5,6,45,42,85,74,41,24,34,85,41,34,74,58,53,7,52,15,42,78,16,53,61,56,64,84,42,45,64,64,62,2,3,6,4,10,41,123,7,52,15,42,78,16,53,61,56,64,84,42,45,64,64,62,2,3,6,4,10,41,123,5,6,45,42,85,74,41,24,34,85,41,34,74,58,53,7,52,15,42,78,16,5,61,56,64,84,42,45,64,64,62,2,62,7,5,9,10,11,36]

maior(numero)