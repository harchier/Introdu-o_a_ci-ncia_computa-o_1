lista1 = ["vermelho", "verde", "azul"]

#forma incorreta
# lista2 = lista1
# print(lista2)
# lista2[0] = "rosa"
# print(lista1)
# print(lista2)

#forma correta
def clone(lista):
    clone = []
    for objeto in lista:
        clone.append(objeto)
    return clone

lista2 = clone(lista1)
print(lista2)

#fatiamento também cria nova lista
#lista1[ini:fim]
#lista1[ini:]
#lista1[:fim]
lista2 = lista1[:] #clona a lista