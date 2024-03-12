#Eu quero que você faça programa que vá receber do usuário, que vai digitar uma sequência de números e para cada número que ele digite eu quero que você imprima o fatorial desse número.
def fatorial(n):
    f = 1
    while(n > 0):
        f *= n
        n -= 1
    return f

while True:
    n = int(input("Digite um número(0 sai): "))
    if(n == 0):
        print(f"Fatorial de 0 = 1")
        break
    else:
        aux = n
        f = fatorial(n)
        print(f"Fatorial de {aux} = {f}")