from  random  import randint
from time import *
import os
def alex_kid():
    f= True
    ale = 0
    bos = 0
    while f:
        intens = ['pedra', 'papel','Tesolra']
        comp = randint(0,2)

        print('''Suas opeções:
        [0] Pedra
        [1] Papel
        [2] Tesolra ''')
        print()
        jogador = int(input("Escolha sua jogada? "))
        if jogador>2:
            print("VALOR INVALIDO!")
        else:
            print("JO")
            sleep(1)
            print("KEEE...")
            sleep(2)
            print("PO!!!")
            sleep(1)
            print()
            print(f"O computador escolheu: {intens[comp]}")
            print(f"O jogador  jogou: {intens[jogador]}")
            print()

            if comp == 0: #computador jogou pedra
                if  jogador == 0:
                    print("EMPATE!")
                
                elif jogador == 1:
                    print("JOGADOR VENCE!")
                    ale += 1
                
                elif jogador == 2:
                    print("COMPUTADOR VENCE!")
                    bos += 1
                    
                else:
                    print("JOGADA INVALIDA!")
                

            elif comp == 1: # computador jogoou Papel
                if  jogador == 0:
                    print("COMPUTADOR VENCE!")
                    bos += 1
                
                elif jogador == 1:
                    print("EMPATE!")
                
                elif jogador == 2:
                    print("JOGADOR VENCE!")
                    ale += 1
                    
                else:
                    print("JOGADA INVALIDA!")

            elif comp == 2: # computador jogou Tesolra
                if  jogador == 0:
                    print("JOGADOR VENCE!")
                    ale += 1
                
                elif jogador == 1:
                    print("COMPUTADOR VENCE!")
                    bos += 1
                
                elif jogador == 2:
                    print("EMPATE!")
                    
                else:
                    print("JOGADA INVALIDA!")
            if ale==3:
                os.system("clear") or None
                print("ALEX KID VENCEU!!")
                f = False
                sleep(3)
            if bos==3:
                f = False
                os.system("clear") or None
                print("BOSS VENCEU!!")
                sleep(3)
    return True
alex_kid()
