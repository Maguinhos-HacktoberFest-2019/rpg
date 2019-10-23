#Importando o módulo time
import time
import random

enigmas = [["cadeado","Não ladra, não morde, mas também não deixa entrar.\nQuem é?\n\n"],
           ["tesoura", "O que tem duas pernas, dois aneis e um prendendor no meio?\n"],
           ["cebola", "Ela veste cem casacos por cima.\nQuem a despir, lágrimas derramará...\nQuem é ela?\n"],
           ["nenhuma","Em uma bétula nasceram 90 maças.\nBateu um vento forte e 10 maçãs caíram.\nQuantas sobraram?\n"]]

#Introdução
def hangman():
    print ("Você chega em um local abandonado e escuro...\nDe longe consegue observar um vulto de uma pessoa suspensa no ar por um corda.")
    time.sleep(6)
    print ("")

    print ("Você corre em direção do indivíduo que clama por ajuda.\nDe repente...\nUm piso falso...\nVocê percebe ter caindo em uma armadilha.")
    time.sleep(6)
    print ("")

    print ("- HAHAHAHAHA! Exclama uma voz medonha escondida nas sombras.")
    time.sleep(6)
    print ("")

    print ("- Resolva meu enigma, aventureiro, e poderá sair livre daqui... Falhe e morrerá! HAHAHAHAHAHA")
    time.sleep(6)
    print ("")

    print ("- Preste muito atenção, aventureiro...\nSó direi uma vez... HAHAHAHAHAHA")
    time.sleep(5)
    print ("")

    indice = random.randint(0, len(enigmas)-1)

    print (enigmas[indice][1])
    time.sleep(10)

    #Resposta
    resposta = enigmas[indice][0]

    #Numero de tentativas
    turnos = 5

    while turnos > 0:         

        tentativa = input("resposta: ").lower()

        if tentativa == resposta:
            print ("")       
            print ("Certa resposta, aventureiro... HAHAHAHA\nVocê não é tão idiota como imaginei...")
            time.sleep(6)
            return True

        else:
            turnos -= 1
            print ("")        
            print ("ERRADO! HAHAHAHA")

            if turnos > 0:
                print ("Você tem apenas ", + turnos, " chance(s) restante(s), aventureiro...")
                print ("")
                time.sleep(2)

            else:
                print ("")           
                print ("HAHAHAHA! Você PERDEU!")
                return False