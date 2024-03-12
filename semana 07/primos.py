#Esse programa verifica se um número é primo
def verifica_inteiro(pergunta):
    while True:
        try:
            inteiro = int(input(pergunta))
            if(inteiro < 0):
                print("O número deve ser positivo")
            else:
                return inteiro
        except Exception:
            print("O valor deve ser um número inteiro!")

def verifica_primo(n):
    i = 1
    divisores = 0
    while(i <= n):
        if(n % i == 0):
            divisores += 1
        i += 1
    if(divisores == 2):
        primo = True
    else:
        primo = False
    return primo

n = verifica_inteiro("Digite a quantidade de primos que deseja: ")

i = 0
primos = 0
while(primos < n):
    e_primo = verifica_primo(i)
    if(e_primo == True):
        print(i, end=" ")
        primos += 1
    i += 1
