def remove_repetidos(lista):
    lista2 = []
    for e in lista:
        if(e not in lista2):
            lista2.append(e)
    lista2.sort()
    return lista2

