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
    if(jogada == 1):
        print(f"\nO computador tirou uma peça.")
    else:
        print(f"\nO computador tirou {jogada} peças")
    return jogada


modo_jogo = int(input("""Bem-vindo ao jogo do NIM! Escolha:

1 - para jogar uma partida isolada
2 - para jogar um campeonato """))

if(modo_jogo == 1):
    max_rodadas = 1
    print("\nVoce escolheu uma partida isolada!")
else:
    max_rodadas = 3
    print("\nVoce escolheu um campeonato!")

pontos_usuario = 0
pontos_cpu = 0
rodada = 1
while(rodada <= max_rodadas):
    print(f"\n**** Rodada {rodada} ****")
    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if(n % (m + 1) == 0):
        print("\nVocê começa!")
        while(n > 0):
            #usuário joga
            while True:
                pecas_tiradas = int(input("\nQuantas peças você vai tirar? "))
                if(0 < pecas_tiradas <= m):
                    break
                else:
                    print("\nOops! Jogada inválida! Tente de novo.")
            
            if(pecas_tiradas == 1):
                print("\nVocê tirou uma peça.")
            else:
                print(f"\nvocê tirou {pecas_tiradas} peças.")
            
            n -= pecas_tiradas
            
            #verifica vitória
            if(n == 1):
                print("Agora resta apenas uma peça no tabuleiro.")
            elif(n == 0):
                print("Fim do jogo! Você ganhou!")
                vencedor = "u"
                pontos_usuario += 1
                break
            else:
                print(f"Agora restam {n} peças no tabuleiro.")
            
            
            #cpu joga
            cpu = jogada_cpu(n, m)
            
            n -= cpu
            
            #verifica vitória
            if(n == 1):
                print("Agora resta apenas uma peça no tabuleiro.")
            elif(n == 0):
                print("Fim do jogo! O computador ganhou!")
                vencedor = "cpu"
                pontos_cpu += 1
                break
            else:
                print(f"Agora restam {n} peças no tabuleiro.")
            

    else:
        print("\nComputador começa!")
        while(n > 0):
            #cpu joga
            cpu = jogada_cpu(n, m)
            
            n -= cpu
            
            #verifica vitória
            if(n == 1):
                print("Agora resta apenas uma peça no tabuleiro.")
            elif(n == 0):
                print("Fim do jogo! O computador ganhou!")
                vencedor = "cpu"
                pontos_cpu += 1
                break
            else:
                print(f"Agora restam {n} peças no tabuleiro.")
            

            #usuário joga
            while True:
                pecas_tiradas = int(input("\nQuantas peças você vai tirar? "))
                if(0 < pecas_tiradas <= m):
                    break
                else:
                    print("\nOops! Jogada inválida! Tente de novo.")
            
            if(pecas_tiradas == 1):
                print("\nVocê tirou uma peça.")
            else:
                print(f"\nvocê tirou {pecas_tiradas} peças.")
            
            n -= pecas_tiradas
            
            #verifica vitória
            if(n == 1):
                print("Agora resta apenas uma peça no tabuleiro.")
            elif(n == 0):
                print("Fim do jogo! Você ganhou!")
                vencedor = "u"
                pontos_usuario += 1
                break
            else:
                print(f"Agora restam {n} peças no tabuleiro.")
    
    rodada += 1        
    
#placar final
if(modo_jogo == 1):
    print("\n**** Final da partida! ****")
else:
    print("\n**** Final do campeonato! ****")

print(f"\nPlacar:Você {pontos_usuario} X Computador {pontos_cpu}")


