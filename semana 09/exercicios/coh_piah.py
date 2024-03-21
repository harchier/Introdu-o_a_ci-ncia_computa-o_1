import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print()
    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    print()
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        print()
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    i = 0
    while i < 6:
        d = abs(as_a[i] - as_b[i])
        soma += d
        i += 1
    sab = soma / 6
    return sab
    

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    data_p = []
    total_frases = 0
    n_caracteres_frase = 0
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            total_frases += 1
            n_caracteres_frase += len(frase)
            palavras = separa_palavras(frase)
            for palavra in palavras:
                data_p.append(palavra)
    
    total_sentencas = len(sentencas)
    total_palavras = len(data_p)

    soma_tamanho_palavras = 0
    for palavra in data_p:
        soma_tamanho_palavras += len(palavra)
    
    n_caracteres_sentenca = 0
    for e in sentencas:
        n_caracteres_sentenca += len(e) 
    
    wal = soma_tamanho_palavras / total_palavras  
    ttr = n_palavras_diferentes(data_p) / total_palavras
    hlr = n_palavras_unicas(data_p) / total_palavras
    sal = n_caracteres_sentenca / total_sentencas
    sac = total_frases / total_sentencas
    pal = n_caracteres_frase / total_frases

    return [wal, ttr, hlr, sal, sac, pal]



def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    valores = []
    i = 0
    while i < len(textos):
        ass_a = calcula_assinatura(textos[i])
        sab = compara_assinatura(ass_a, ass_cp)
        valores.append(sab)
        i += 1
    e = 0
    min = float('inf')
    while e < len(valores):
        if(valores[e] < min):
            min = valores[e]
        e += 1
    saida = valores.index(min) + 1
    return saida

def main():
    ass_cp = le_assinatura()

    textos = le_textos()

    avaliacao = avalia_textos(textos, ass_cp)
    print()
    print(avaliacao)

main()

