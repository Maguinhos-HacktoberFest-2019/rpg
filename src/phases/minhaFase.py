# autor: Mellyssa

import sys 

def minhaFase():
    pontos = 0

    print("\n==== Quem é o intruso?====\n")
    print("Nesse jogo, seu objetivo é descobrir, dentre as opções, qual delas não faz parte do conjunto")
    print("Lembre-se: Você tem UMA única chance.")
    print("Por isso, pense BEM antes de responder")
    print("Bora jogar????")


#validando as opções do jogador
def resposta(r):
    if(r != "A" and r != "B" and r != "C" and r != "D" and r != "E"):
        print("Opção inválida, ")
        r = input("Entre com alguma das opções válidas: ").upper()
        return resposta(r)
    else:
        return r

def pergunta1():
    print("Pergunta 1")
    print("Qual nome não pertence ao conjunto?")
    r = input("A) José\nB) Paulo\nC) Maria\nD) Luísa\nE) Carlos")
    r = resposta(r)
    return r

def pergunta2():
    print("Pergunta 2")
    print("Qual letra não pertence ao conjunto?")
    r = input("A) A\nB) B\nC) T\nD) G\n E)P")
    r = resposta(r)
    return r

def pergunta3():
    print("Pergunta 3")
    print("Qual super herói não pertence ao conjunto?")
    r = input()
    r = resposta(r)
    return r

def pergunta4():
    print("Pergunta 4")
    print("Qual número não pertence ao conjunto?")
    r = input()
    r = resposta(r)
    return r

def pergunta5():
    print("Pergunta 5")
    print("Qual time não pertence ao conjunto?")
    r = input()
    r = resposta(r)
    return r

def pergunta6():
    print("Pergunta 6")
    print("Qual país não pertence ao conjunto?")
    r = resposta(r)
    r = input()
    return r

def pergunta7():
    print("Pergunta 7")
    print("Qual número não pertence ao conjunto?")
    r = input()
    r = resposta(r)
    return r

def pergunta8():
    print("Pergunta 8")
    print("Qual seleção de futebol não pertence ao conjunto?")
    r = input()
    r = resposta(r)
    return r


