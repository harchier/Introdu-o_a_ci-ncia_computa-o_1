n = int(input("Digite o número a fatorar: "))
i = 2
while n > 1:
    multiplicidade = 0
    while(n % i == 0):
        multiplicidade += 1
        n = n / i    
    if(multiplicidade != 0):
        print(f"Fator = {i} Multiplicidade = {multiplicidade}")
    i += 1
    

