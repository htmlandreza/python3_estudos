def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"] # 6 espaços

    enforcou = False
    acertou = False
    print(letras_acertadas)

    while(not enforcou and not acertou):
        index = 0
        chute = input("Qual letra?")
        chute = chute.strip()

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim do Jogo!")

if(__name__ == "__main__"):
    jogar()