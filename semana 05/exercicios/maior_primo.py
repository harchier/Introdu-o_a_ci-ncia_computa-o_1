def maior_primo(range):
    k = 0
    while k <= range:
        divisores = 0
        i = 1
        while i <= k:
            if k % i == 0:
                divisores += 1
            i += 1
        if divisores == 2:
            maior_primo = k
        k += 1
    return maior_primo

   



