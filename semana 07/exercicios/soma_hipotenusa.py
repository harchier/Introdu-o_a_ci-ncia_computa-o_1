def e_hipotenusa(n):
    i = 1
    hipotenusa = False
    while(i < n):
        j = 1
        while(j < n):
            if((n ** 2) == (i**2) + (j**2)):
                hipotenusa = True
            j += 1
        i += 1
    return hipotenusa

def soma_hipotenusas(n):
    i = 1
    soma = 0
    while(i <= n):
        h = e_hipotenusa(i)
        if(h == True):
            soma += i
        i += 1
    return soma
