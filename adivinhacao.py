import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_tentativas = 3
#print(numero_secreto)

print("Qual nível deseja?")


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
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto.", end="\n\n")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto.", end="\n\n")

print("Fim do Jogo!")


