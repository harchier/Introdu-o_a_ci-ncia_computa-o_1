#Faça um programa que leia uma sequencia de números terminados em 0 e quando digitado 0 retorne essa lista invertida.

def verifica_entrada(pergunta):
    lista = []
    while True:
        try:
            entrada = int(input(pergunta))
            print("=" * 43)
            if(entrada % 10 == 0) and (entrada != 0):
                lista.append(entrada)
            elif(entrada == 0):
                break
            else:
                print("A entrada deve ser um número multiplo de 10.")
        except Exception:
            print("A entrada deve ser um número.")
    return lista

def inverte_lista(lista):
    lista_invertida = []
    i = 1
    while(i <= len(lista)):
        lista_invertida.append(lista[-i])
        i += 1
    return lista_invertida

def main():
    print("-" * 100)
    print(f"{'Esse programa inverte uma lista digitada pelo usuário.':^100}")
    print("-" * 100)
    
    lista = verifica_entrada("Digite um número multiplo de 10 (0 sai): ")
    
    lista_invertida = inverte_lista(lista)
    
    print(f"Lista original  = {lista}")
    print(f"Lista invertida = {lista_invertida}")

main()