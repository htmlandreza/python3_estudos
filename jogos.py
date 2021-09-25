import adivinhacao
import forca

print("********************")
print("Escolha o seu jogo!")
print("********************")

print("(1) Adivinhação (2) Forca")
jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogo de Adivinhação")
    adivinhacao.jogar()
elif(jogo == 2):
    print("Jogo de Forca")
    forca.jogar()

