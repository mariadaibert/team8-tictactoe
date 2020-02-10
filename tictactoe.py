###importar funções
import avaliar_jogada2
import deu_velha
import jogada

### Declarar matriz do jogo
matriz = [[100,100,100],[100,100,100],[100,100,100]]
for linha in matriz:
    print(linha)
    
#Declarar peças dos jogadores
player1=1
player2=20

#Repetição até alguém ganhar ou dar velha
velha=0
while(velha==0):
        
    #Atualiza jogo com jogada Player1 peça:1
    matriz = jogada.jogar(player1,matriz)      

    #Testar se Player1 ganhou ou se deu velha
    if(avaliar_jogada2.avaliar(player1,matriz)==True):
        break
        
    #Atualizar jogo com jogada Player2 peça:20    
    matriz = jogada.jogar(player2,matriz)

    #Testar se Player2 ganhou ou se deu velha
    if(avaliar_jogada2.avaliar(player2,matriz)==True):
        break