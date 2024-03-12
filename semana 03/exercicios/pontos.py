import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
d = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
if d >= 10:
    print("longe")
else:
    print("perto")