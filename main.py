### Declarar matriz do jogo
matriz = [[100,100,100],[100,100,100],[100,100,100]]

#Repetição até alguém ganhar ou dar velha
velha=0
while(velha==0):
    
    for linha in matriz:
        print(linha)

    #Atualizar jogo com jogada Player1 peça:2    
    x=int(input("Player 1 - Linha:"))
    y=int(input("Player 1 - Coluna:"))
    matriz[x-1][y-1]=2

    #Testar se Player1 ganhou 
    i=0
    while(i<3):
        if(sum(matriz[i])==6):
            print("Player 1 ganhou. Linha",i+1)
            velha=1
            break
        else:
            j=0
            col=0
            dia1=0
            dia2=0
            while(j<3):
                if(i==j):
                    dia1=dia1+matriz[i][j]  
                if(i+j==2):
                    dia2=dia2+matriz[i][j]
                col=col+matriz[j][i]
                j=j+1

            if(dia1==6):
                print("Player 1 ganhou. Diagonal Principal")
                velha=1
                break
            elif(dia2==6):
                print("Player 1 ganhou. Diagonal Secundária")
                velha=1
                break
            elif(col==6):
                print("Player 1 ganhou. Coluna",i+1)
                velha=1
                break
        i=i+1


    for linha in matriz:
        print(linha)
        
    #Atualizar jogo com jogada Player2 peça:1
    x=int(input("Player 2 - Linha:"))
    y=int(input("Player 2 - Coluna:"))
    matriz[x-1][y-1]=1

    #Testar se Player2 ganhou
    i=0
    while(i<3):
        if(sum(matriz[i])==3):
            print("Player 2 ganhou. Linha",i+1)
            velha=1
            break
        else:
            j=0
            col=0
            dia1=0
            dia2=0
            while(j<3):
                if(i==j):
                    dia1=dia1+matriz[i][j]  
                if(i+j==2):
                    dia2=dia2+matriz[i][j]
                col=col+matriz[j][i]
                j=j+1

            if(dia1==3):
                print("Player 2 ganhou. Diagonal Principal")
                velha=1
                break
            elif(dia2==3):
                print("Player 2 ganhou. Diagonal Secundária")
                velha=1
                break
            elif(col==3):
                print("Player 2 ganhou. Coluna",i+1)
                velha=1
                break
        i=i+1