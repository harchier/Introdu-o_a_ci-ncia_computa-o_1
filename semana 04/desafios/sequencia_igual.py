print("Essa programa informa se um sequência possui numeros adjacentes iguais.")
n = int(input("Digite um sequência de números inteiros: "))

possui_sequencia_igual = False
while n > 0:
    ultimo = n % 10
    penultimo = (n % 100) // 10
    if(ultimo == penultimo):
        possui_sequencia_igual = True
    n = n // 10

if(possui_sequencia_igual == True):
    print("A sequência possui números adjacentes iguais.")
else:
    print("A sequência não possui números adjacents iguais.")