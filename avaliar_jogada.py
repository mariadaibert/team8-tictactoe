#Avaliar se jogador ganhou após sua jogada ou se deu velha
def avaliar(jogador,matriz):
    i=0
    dia1=0
    dia2=0
    vitoria=False
    criterio=3*jogador
    while(i<3):
        if(sum(matriz[i])==criterio):
            print("Player "+str(jogador)+" ganhou. Linha"+str(i+1))
            vitoria=True
            break
        else:
            j=0
            col=0
            while(j<3):
                if(i==j):
                    dia1=dia1+matriz[i][j]  
                if(i+j==2):
                    dia2=dia2+matriz[i][j]
                col=col+matriz[j][i]
                j=j+1

            if(dia1==criterio):
                print("Player "+str(jogador)+" ganhou. Diagonal Principal")
                vitoria=True
                break
            elif(dia2==criterio):
                print("Player "+str(jogador)+" ganhou. Diagonal Secundária")
                vitoria=True
                break
            elif(col==criterio):
                print("Player "+str(jogador)+" ganhou. Coluna "+str(i+1))
                vitoria=True
                break
        i=i+1
                      
    for linha in matriz:
        print(linha)
        
    return vitoria