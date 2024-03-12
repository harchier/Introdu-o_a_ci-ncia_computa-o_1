import math

print("Esse programa calcula as raízes de um equação do segundo grau.")
print("ax^2 + bx + c = 0")
print("="*50)
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = (b ** 2) - (4 * a * c)

print("="*50)
if(delta < 0):
    print("A equação não possui raízer reais.")
elif(delta == 0):
    x = (-b) / (2 * a)
    print("A equação possui uma única raiz.")
    print(f"S = [{x}]")
else:
    x1 = ((-b) + (math.sqrt(delta))) / (2 * a)
    x2 = ((-b) - (math.sqrt(delta))) / (2 * a)
    print("A equação possui duas raízes reais.")
    print(f"S = [{x2, x1}]")

