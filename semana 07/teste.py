def e_hipotenusa(n):
    i = 1
    hipotenusa = False
    while(i < n):
        j = 1
        while(j < n):
            if((n ** 2) == (i**2) + (j**2)):
                hipotenusa = True
                print(f"h = {n}, i = {i}, j = {j}")
            j += 1
        i += 1
    return hipotenusa

# while True:
#     x = int(input("Digite o teste: "))
#     teste = e_hipotenusa(x)
#     print(teste)
#     if(x == 0):
#         break

def soma_hipotenusa(n):
    i = 1
    soma = 0
    while(i <= n):
        h = e_hipotenusa(i)
        if(h == True):
            soma += i
        i += 1
    return soma

x = int(input("Digite o teste: "))
teste = soma_hipotenusa(x)
print(teste)