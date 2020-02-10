#Captura jogada
def jogar(peca_jogador,matriz):
    inv=1
    while(inv==1):
        print("Jogue, Player"+str(peca_jogador))
        x=int(input("Linha:"))
        y=int(input("Coluna:"))
        if(matriz[x-1][y-1]==100):
            matriz[x-1][y-1]=peca_jogador
            inv=0
        else:
            print("Jogada inválida.")
    return matriz
