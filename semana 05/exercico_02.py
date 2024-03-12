#reorganizar o código que calcula as raízes de 2 grau

def raizes(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if(delta < 0):
        print("A equação não possui raízes reais.")
    elif(delta == 0):
        x = (-b) / (2 * a)
        print(f"S = [{x}]")
    else:
        x1 = ((-b) + (delta ** (1/2))) / (2 * a)
        x2 = ((-b) - (delta ** (1/2))) / (2 * a)
        print(f"S = [{x1},{x2}]")

def main():
    print("Esse programa calcula as raízes de um equação do segundo grau.")
    print("ax^2 + bx + c = 0")
    print("="*50)
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    raizes(a, b, c)



