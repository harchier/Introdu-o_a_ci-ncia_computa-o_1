def maior_elemento(lista):
    maior = lista[0]
    for e in lista:
        if(e > maior):
            maior = e
    return maior

