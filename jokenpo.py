from random import randint
while True:
    try:
        itens = ("Pedra", "Papel", "Tesoura")
        computador = randint(0, 2)
        print(" ")
        print("""Suas opções:
        [0] Pedra
        [1] Papel
        [2] Tesoura
        """)
        jogador= (input("Qual será sua jogada? "))
        if jogador == "sair":
            print("VOCÊ SAIU DO JOGO!")
            break
        jogador_int = int(jogador)
        while jogador_int != 0 and jogador_int != 1 and jogador_int != 2:
            print("ESCOLHA UMA OPÇÃO VALIDA!")
            jogador= (input("Qual será sua jogada? "))
            jogador_int = int(jogador)
        print("-=" * 11)

        if jogador_int == 0:
            print("Jogador escolheu Pedra")
            if computador == 2:
                print(f"Computador escolheu {itens[computador]}")
                print("-=" * 11)
                print("***JOGADOR VENCEU***")
            elif computador == 1:
                print(f"Computador escolheu {itens[computador]}")
                print("-=" * 11)
                print("***COMPUTADOR VENCEU***")
            else:
                print(f"Computador escolheu {itens[computador]}")
                print("-=" * 11)
                print("***EMPATE***")

        if jogador_int == 1:
            print("Jogador escolheu Papel")
            if computador == 0:
                print(f"Computador escolheu {itens[computador]}")
                print("-=" * 11)
                print("***JOGADOR VENCEU***")
            elif computador == 2:
                print(f"Computador escolheu {itens[computador]}")
                print("-=" * 11)
                print("***COMPUTADOR VENCEU***")
            else:
                print(f"Computador escolheu {itens[computador]}")
                print("-=" * 11)
                print("***EMPATE***")

        if jogador_int == 2:
            print("Jogador escolheu Tesoura")
            if computador == 1:
                print(f"Computador escolheu {itens[computador]}")
                print("-=" * 11)
                print("***JOGADOR VENCEU***")
            elif computador == 0:
                print(f"Computador escolheu {itens[computador]}")
                print("-=" * 11)
                print("***COMPUTADOR VENCEU***")
            else:
                print(f"Computador escolheu {itens[computador]}")
                print("-=" * 11)
                print("***EMPATE***")
    except:
        print("ESCOLHA UMA OPÇÃO VALIDA!")   
        continue  