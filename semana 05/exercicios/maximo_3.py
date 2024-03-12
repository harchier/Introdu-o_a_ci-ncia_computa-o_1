def maximo(x, y, z):
    if(x >= y) and (x >= z):
        max = x
    elif(y >= x) and (y >= z):
        max = y
    elif(z >= x) and (z >= y):
        max = z
    return max

