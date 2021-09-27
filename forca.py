def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        index = 0
        chute = input("Qual letra?")
        chute = chute.strip()

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("jogando ...")

    print("Fim do Jogo!")

    if(__name__ == "__main__"):
        jogar()