#programa para calcular o coeficiente binomial

def fatorial(x):
    f = 1
    while x > 0:
        f *= x
        x -= 1
    return f

def verifica_inteiro(pergunta):
    while True:
        try:
            n = int(input(pergunta))
            if(n >= 0):
                return n
            else:
                print("Deve ser um número Natural.")
        except Exception:
            print("Deve ser um número!")

print("Esse programa calcula o coeficiente binomial.")
n = verifica_inteiro("Digite o valor de n: ")
k = verifica_inteiro("Digite o valor de k: ")

coeficiente_binomial = (fatorial(n)) / ((fatorial(n - k)) * fatorial(k))

print(f"O coeficiente binomial é: {coeficiente_binomial}")