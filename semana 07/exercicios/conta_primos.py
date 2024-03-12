def n_primos(n):
    primos = 0
    i = 2
    while(i <= n):
        divisores = 0
        j = 1
        while(j <= i):
            if(i % j == 0):
                divisores += 1
            j += 1
        if(divisores == 2):
            primos += 1
        i += 1
    return primos

print(n_primos(2))

print(n_primos(4))

print(n_primos(121))

