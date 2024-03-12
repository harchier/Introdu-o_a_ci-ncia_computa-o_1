n = int(input("Digite um número inteiro: "))
adjacentes = False
while n > 0:
    ultimo = n % 10
    penultimo = (n % 100) // 10
    if ultimo == penultimo:
        adjacentes = True
    n = n // 10
if adjacentes:
    print("sim")
else:
    print("não")