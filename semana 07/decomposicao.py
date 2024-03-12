#Dado um número intiero n, n > 1, imprimir sua decomposição em fatores primos, indicando também a multiplicidade de cada fator.
#8 = 2 * 2 * 2
#20 = 2 * 2 * 5
#1000 = 2**3 * 5 **3

n = int(input("Digite o número a fatorar: "))
aux = n
lista = []
multiplicidade = 0
while n > 1:
    i = 2
    while(n % i != 0):
        i += 1
    lista.append(i)
    n = n / i

print(f"{aux} =",end=" ")   
print(*lista,sep=" x ")



    