l = int(input("digite a largura: "))
a = int(input("digite a altura: "))
i = 1
while(i <= a):
    j = 1
    while(j <= l):
        if(i > 1) and (i < a):
            if(j > 1) and (j < l):
                print(" ",end="")
            else:
                print("#",end="")
        else:
            print("#",end="")
        j += 1
    print()
    i += 1