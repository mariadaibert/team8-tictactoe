#Captura jogada
import jogada

def jogar(peca_jogador,matriz):
    print("Jogue, Player "+str(peca_jogador))
    x=int(input("Linha:"))
    y=int(input("Coluna:"))
    if(matriz[x-1][y-1]==100):
        matriz[x-1][y-1]=peca_jogador
    else:
        print("Jogada inválida.")
        jogada.jogar(peca_jogador,matriz)
    
    return matriz
