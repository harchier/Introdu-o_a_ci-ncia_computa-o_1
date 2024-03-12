n = int(input("Digite um número inteiro: "))
soma = 0
while n != 0:
    ultimo = n % 10
    soma += ultimo
    n = n // 10
print(soma)