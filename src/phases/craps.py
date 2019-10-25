#autor: Felipe Becalli Trindade.

from random import randint

def craps():
    print("O jogador lança um par de dados, obtendo um valor entre 2 a 12.\nSe, na primeira jogada, você tirar 7 ou 11, você recebe um 'natural' e ganhou.\nSe você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de 'craps' e você perdeu.\nSe, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu 'Ponto'.\nCom um 'Ponto' o objetivo agora é continuar jogando os dados até tirar este número novamente.\nVocê perde, no entanto, se tirar um 7 antes de tirar o 'Ponto' novamente.")
    print("Jogue o dado!")
    input("Pressione ENTER para jogar o dado: ")
    x=randint(1,12)
    if x == 7 or x == 11:
        print("Natural! Você ganhou!", "Seu número foi", x)
    elif x == 2 or x == 3 or x == 12:
        print("Craps! Você perdeu!",  "Seu número foi", x)
    else:
        print("Vocẽ marcou um 'Ponto'",  "Seu número foi", x)
        input("Pressione ENTER para jogar o dado: ")
        y = 0
        while y != x:
            y=randint(1,12)
            if y == x:
                print("Você marcou 2 pontos parabéns foi ganhou.", "Seu número foi", y)
            elif y == 7:
                print("Craps! Você perdeu!", "Seu número foi 7")
                break
            else:
                print("Seu número dessa vez foi", y)
                input("Aperte ENTER para jogar o Dado novamente: ")
