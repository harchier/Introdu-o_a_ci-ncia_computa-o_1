def monta_lista(pergunta):
    lista = []
    while True:
        try:
            entrada = int(input(pergunta))
            if(entrada == 0):
                break
            lista.append(entrada)
        except Exception:
            print("A entrada deve ser um número inteiro.")
    return lista

def inverte_lista(lista):
    lista_invertida = []
    i = 1
    while(i <= len(lista)):
        lista_invertida.append(lista[-i])
        i += 1
    return lista_invertida

def main():
    lista = monta_lista("Digite um número: ")
    lista_invertida = inverte_lista(lista)
    print()
    for e in lista_invertida:
        print(e)

main()