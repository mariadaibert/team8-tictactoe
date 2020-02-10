#Testa se deu velha
def deu_velha(matriz):
    if(sum(matriz[0])+sum(matriz[1])+sum(matriz[2])<100):
        print("Deu velha!")
        return True