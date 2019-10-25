from  random  import randint
from time import *
def alex_kid():
    intens = ['pedra', 'papel','Tesolra']
    comp = randint(0,2)

    print('''Suas opeções:
    [0] Pedra
    [1] Papel
    [2] Tesolra ''')
    print()
    jogador = int(input("Escolha sua jogada? "))
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
        
        elif jogador == 2:
            print("COMPUTADOR VENCE!")
            
        else:
            print("JOGADA INVALIDA!")
        

    elif comp == 1: # computador jogoou Papel
        if  jogador == 0:
            print("COMPUTADOR VENCE!")
        
        elif jogador == 1:
            print("EMPATE!")
        
        elif jogador == 2:
            print("JOGADOR VENCE!")
            
        else:
            print("JOGADA INVALIDA!")

    elif comp == 2: # computador jogou Tesolra
        if  jogador == 0:
            print("JOGADOR VENCE!")
        
        elif jogador == 1:
            print("COMPUTADOR VENCE!")
        
        elif jogador == 2:
            print("EMPATE!")
            
        else:
            print("JOGADA INVALIDA!")
    return True
alex_kid()