def computador_escolhe_jogada(n, m):
    i = 1
    while i <= m:
        if((n - i) % (m + 1) == 0):
            jogada = i
            break
        else:
            i += 1
    else:
        jogada = m
    if(jogada == 1):
        print(f"\nO computador tirou uma peça.")
    else:
        print(f"\nO computador tirou {jogada} peças")
    return jogada

def usuario_escolhe_jogada(n, m):
    while True:
        pecas_tiradas = int(input("\nQuantas peças você vai tirar? "))
        if(0 < pecas_tiradas <= m):
            break
        else:
            print("\nOops! Jogada inválida! Tente de novo.")
        
    if(pecas_tiradas == 1):
        print("Você tirou uma peça.")
    else:
        print(f"Você tirou {pecas_tiradas} peças.")
    return pecas_tiradas

def verifica_vitoria(n, jogador):
    if(n == 1):
        print("Agora resta apenas uma peça no tabuleiro.")
    elif(n == 0):
        if(jogador == "usuario"):
            print("Fim do jogo! Você ganhou!")
            vencedor = "u"
            return vencedor
        else:
            print("Fim do jogo! O computador ganhou!")
            vencedor = "cpu"
            return vencedor
    else:
        print(f"Agora restam {n} peças no tabuleiro.")

def partida():
    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if(n % (m + 1) == 0):
        print("\nVocê começa!")
        venceu = False
        while(n > 0) and (venceu == False):
            jogada_usuario = usuario_escolhe_jogada(n, m)
            
            n -= jogada_usuario

            vencedor = verifica_vitoria(n, "usuario")
            if(vencedor != None):
                break
            
            jogada_cpu = computador_escolhe_jogada(n, m)

            n -= jogada_cpu

            vencedor = verifica_vitoria(n, "cpu")
            if(vencedor != None):
                break
            
    else:
        print("\nComputador começa!")
        venceu = False
        while(n > 0) and (venceu == False):
            jogada_cpu = computador_escolhe_jogada(n, m)

            n -= jogada_cpu

            vencedor = verifica_vitoria(n, "cpu")
            if(vencedor != None):
                break
            
            jogada_usuario = usuario_escolhe_jogada(n, m)
            
            n -= jogada_usuario

            vencedor = verifica_vitoria(n, "usuario")
            if(vencedor != None):
                break
    return vencedor
                       
def campeonato():
    pontos_usuario = 0
    pontos_cpu = 0
    rodada = 1
    while(rodada <= 3):
        print(f"\n**** Rodada {rodada} ****")
        vencedor = partida()
        if(vencedor == "cpu"):
            pontos_cpu += 1
        else:
            pontos_usuario += 1
        rodada += 1
    print("\n**** Final do campeonato! ****")
    print(f"\nPlacar: Você {pontos_usuario} X {pontos_cpu} Computador")

modo_jogo = int(input("""Bem-vindo ao jogo do NIM! Escolha:

1 - para jogar uma partida isolada
2 - para jogar um campeonato """))

if(modo_jogo == 1):
    print("\nVoce escolheu uma partida isolada!")
    partida()
else:
    print("\nVoce escolheu um campeonato!")
    campeonato()