def jogada_cpu(n, m):
    i = 1
    while i <= m:
        if((n - i) % (m + 1) == 0):
            jogada = i
            break
        else:
            i += 1
    else:
        jogada = m
    print(f"Jogada cpu {jogada}")


def verifica_vitoria(n,jogador):
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

def escolhe_modalidade():
    modo_jogo = int(input("""Bem-vindo ao jogo do NIM! Escolha:

    1 - para jogar uma partida isolada
    2 - para jogar um campeonato """))

    if(modo_jogo == 1):
        max_rodadas = 1
        print("\nVoce escolheu uma partida isolada!")
    else:
        max_rodadas = 3
        print("\nVoce escolheu um campeonato!")
    return max_rodadas