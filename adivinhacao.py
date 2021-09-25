import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    #print(numero_secreto)
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina um nível:"))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5


    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute_str = input("Digite o seu número de 1 a 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        # validando entradas
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!", end="\n\n")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior que o número secreto.", end="\n\n")
                if(rodada == total_tentativas):
                    print("O número secreto é {}. Você fez {} pontos!".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! Seu chute foi menor que o número secreto.", end="\n\n")
                if (rodada == total_tentativas):
                    print("O número secreto é {}. Você fez {} pontos!".format(numero_secreto, pontos))
            # número absoluto
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do Jogo!")

if (__name__ == "__main__"):
    jogar()


