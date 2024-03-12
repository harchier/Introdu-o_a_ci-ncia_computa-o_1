print("Esse programa mostra a soma de uma sequecia de números inteiros.")

n = int(input("Digite a sequência de números(ex: 12345): "))

#numero de digitos
d = 10
e = 1
n_digitos = 0
while e != 0:
    e = n // d
    n_digitos += 1
    d *= 10

print(f"Numero de digitos: {n_digitos}")

#soma da sequência
soma = 0
resto = 10
divisor = 1
i = 0
while i < n_digitos:
    operacao = ((n % resto) // divisor)
    soma += operacao
    resto *= 10
    divisor *= 10
    i += 1

print(f"Soma da sequência: {soma}")