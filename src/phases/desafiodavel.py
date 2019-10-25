def desafio():
    resposta = ""
    i = 0
    loop = 1

    while((loop)==1):
        
        print("= Dilema 1 =\n")
        print("A mulher de Zezinho está grávida e queria comer banana com mel, entao mandou ele ir comprar pao na mercearia de Seu Joao.")
        print("Chegando lá, ele tinha 4 opçoes. Digite de 1 a 4 a resposta mais adequada.\n")
        print("1 - Ele deve comprar pao, banana e leite, que custam 8 reais no total, porque estavam na promoçao.")
        print("2 - Ele deve comprar mel, banana e leite, que custam 12 reais no total.")
        print("3 - Ele deve comprar somente banana e mel, que custam 2 reais no total.")
        print("4 - Ele deve comprar somente pao, que custam 11 reais no total.")
    
        i = int(input("Digite a sua resposta:  "))
        resposta = resposta +i


        print("= Dilema 2 =\n")
        print("Na volta pra casa, tinha um cachorro bravo que saiu correndo atrás de Zezinho.")
        print("Nao iria dar tempo de ir no casamento de seu irmao, se ele demorar na mercearia.\n")
        print("1 - Ele deve deixar a bicicleta e ir com os produtos.")
        print("2 - Ele deve enfrentar o cachorro com os produtos.")
        print("3 - Ele deve levar uma mordida do cachorro pra chegar a tempo de ir no casamento de seu irmao.")
        print("4 - Ele nao deve ir no casamento .")
        
        i = int(input("Digite a sua resposta:  "))
        resposta = resposta +i


        print("= Dilema 3 =\n")
        print("Ele chega no casamento após levar os produtos para ela.")
        print("A mulher dele estava sempre organizando a festa e nao tinha como prestar atençao em Zezinho, enquanto uma convidada estava piscando.\n")
        print("1 - Ele deve ignorar a sua mulher.")
        print("2 - Ele deve contar pra sua mulher sobre o ocorrido.")
        print("3 - Ele deve trair a sua mulher, levando a convidada para o banheiro.")
        print("4 -  Ele deve levar um lenço para a convidada.")
        i = int(input("Digite a sua resposta:  "))
        resposta = resposta + i


        print("= Dilema 4 =\n")
        print("Após o casamento, Zezinho e sua mulher finalmente chegam em casa.")
        print("Sua mulher pergunta quem era a convidada da festa, que ela viu piscando para Zezinho.\n")
        print("1 - Ele diz que nao precisa se preocupar, pois era uma amiga de infância.")
        print("2 - Ele diz que nao precisa se preocupar, pois era sua sogra .")
        print("3 - Ele nao deve falar nada.")
        print("4 - Ele diz que nao precisa se preocupar, pois a convidada tinha problema de vista.")
        
        
        i = int(input("Digite a sua resposta:  "))
        resposta = resposta +i


        if((resposta)=="4144"):
            loop = 0
            print("Parabéns, você venceu!!")
            return True

desafio()
