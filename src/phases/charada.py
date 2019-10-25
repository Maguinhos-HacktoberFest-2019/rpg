import os
def charada():
    os.system('clear')
    print('Você procurou a sua vida toda pela cidade das joias de Rubiris, mas quando você finalmente a encontrou e se posicionou para abrir a porta, vocẽ escuta uma voz: "Responda minha pergunta corretamente ou vai morrer sem nunca pisar em Rubiris, você tem apenas 3 chances..."\nPreste muita atenção...\n')
    print('O que é maior que seu maior sonho, pior que o seu pior pesadelo, os pobres não tem, e os ricos não precisam?\n')
    resposta = input("Qual sua resposta? ").lower()
    for x in range(3,-1,-1):
        if resposta == "nada":
            acertou = True
        elif x==1:
            print("Você errou, ser inferior, aceite sua morte!")
            return acertou
        else:
            acertou = False
            print("vocẽ errou, e tem apenas %d chances!"%(x-1))
            resposta = input("Qual sua resposta? ").lower()
    return resposta




