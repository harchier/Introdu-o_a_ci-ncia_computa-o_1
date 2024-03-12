import math
a = float(input())
b = float(input())
c = float(input())
delta = (b**2) - (4*a*c)
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    if delta == 0:
        x = (-b) / (2*a)
        print("a raiz desta equação é",x)
    else:
        x = ((-b) - (math.sqrt(delta))) / (2*a)
        y = ((-b) + (math.sqrt(delta))) / (2*a)
        print("as raízes da equação são",x,"e",y)