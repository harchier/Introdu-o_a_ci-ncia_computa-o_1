min = 6
i = 0
while i < 5:
    n = int(input("Digite um número"))
    if(n < min):
        min = n
    i += 1

print(min)