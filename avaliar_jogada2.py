#Avaliar se jogador ganhou após sua jogada ou se deu velha
import deu_velha

def avaliar(jogador,matriz):
    fim=False
    criterio=3*jogador
    
    if(deu_velha.deu_velha(matriz)==True):
        fim=True
    else:
        soma_linhas=[sum(x) for x in matriz]
        soma_colunas=[sum(x) for x in zip(*matriz)]
        soma_dia1=sum(matriz[i][i] for i in range(3))
        soma_dia2=sum(matriz[i][3-i-1] for i in range(3)) 

        if criterio in soma_linhas:
            print("Player "+str(jogador)+" ganhou. Linha "+str(soma_linhas.index(criterio)+1))
            fim=True
        elif criterio in soma_colunas:
            print("Player "+str(jogador)+" ganhou. Coluna "+str(soma_colunas.index(criterio)+1))
            fim=True
        elif criterio==soma_dia1:
            print("Player "+str(jogador)+" ganhou. Diagonal Principal")
            fim=True
        elif criterio==soma_dia2:
            print("Player "+str(jogador)+" ganhou. Diagonal Secundária")
            fim = True
            
    for linha in matriz:
        print(linha)

    return fim