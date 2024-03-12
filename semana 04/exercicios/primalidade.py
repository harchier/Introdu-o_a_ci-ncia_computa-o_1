n = int(input("Digite um número inteiro: "))
divisores = 0
i = 1
while i <= n:
    if n % i == 0:
        divisores += 1
    i += 1
if divisores == 2:
    print("primo")
else:
    print("não primo")