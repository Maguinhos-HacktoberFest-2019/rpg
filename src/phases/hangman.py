#Importando o módulo time
import time

#Introdução
def hangman():
    print ("Você chega em um local abandonado e escuro...\nDe longe consegue observar um vulto de uma pessoa suspensa no ar por um corda.\n")
    time.sleep(6)
    print ("")
    print ("Você corre em direção do indivíduo que clama por ajuda.\nDe repente...\nUm piso falso...\nVocê percebe ter caindo em uma armadilha.")
    time.sleep(6)
    print ("")

    print ("- HAHAHAHAHA! Exclama uma voz medonha escondida nas sombras.")
    time.sleep(7)
    print ("")

    print ("- Resolva meu enigma, aventureiro, e poderá sair livre daqui... Falhe e morrerá!\nHAHAHAHAHAHA")
    time.sleep(7)
    print("")

    print ("- Preste muito atenção, aventureiro...\nSó direi uma vez...HAHAHAHAHAHA")
    time.sleep(5)
    print ("")

    print ("Não ladra, não morde, mas também não deixa entrar.\nQuem é?")
    time.sleep(10)

    #Resposta
    resposta = "cadeado"

    #Numero de tentativas
    turnos = 5

    while turnos > 0:         

        tentativa = input("resposta: ")

        if tentativa == resposta:
            print("")       
            print ("Certa resposta, aventureiro... HAHAHAHA\nVocê não é tão idiota como imaginei...")
            time.sleep(6)
            return True
        else:
            if turnos > 0:
                turnos -= 1
                print("")        
                print ("ERRADO! HAHAHAHA")    
                print ("Você tem apenas", + turnos, 'chances restantes, aventureiro...')
                print("")
                time.sleep(4)

            else:
                print("")           
                print ("HAHAHAHA! Você PERDEU!")
                return False