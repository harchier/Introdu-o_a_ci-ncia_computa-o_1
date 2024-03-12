print("Esse programa mostra a soma de uma sequecia de números inteiros.")

n = int(input("Digite a sequência de números(ex: 12345): "))

soma = 0
while n > 0:
    ultimo = n % 10
    soma += ultimo
    n = n // 10

print(soma)