# autor: Mellyssa Stephanny de Jesus Mendes

import time
import sys 

#validando as opções do jogador
def resposta(r):
    if(r != "A" and r != "B" and r != "C" and r != "D" and r != "E"):
        print("Opção inválida!")
        r = input("Entre com alguma das opções válidas: ").upper()
        return resposta(r)
    else:
        return r

def pergunta1():
    print("## Pergunta 1 ##")
    print("Qual nome não pertence ao conjunto?")
    r = input("A) José\nB) Paulo\nC) Maria\nD) Luísa\nE) Carlos\n\n")
    r = resposta(r)
    return r

def pergunta2():
    print("## Pergunta 2 ##")
    print("Qual letra não pertence ao conjunto?")
    r = input("A) A\nB) B\nC) T\nD) G\nE) P\n\n")
    r = resposta(r)
    return r

def pergunta3():
    print("## Pergunta 3 ##")
    print("Qual super herói não pertence ao conjunto?")
    r = input("A) Batmam\nB) SuperMan\nC) Flash\nD) Thanos\nE) Hulk\n\n")
    r = resposta(r)
    return r

def pergunta4():
    print("## Pergunta 4 ##")
    print("Qual número não pertence ao conjunto?")
    r = input("A) 303\nB) 81\nC) 234\nD) 11\nE) 15\n\n")
    r = resposta(r)
    return r

def pergunta5():
    print("## Pergunta 5 ##")
    print("Qual país não pertence ao conjunto?")
    r = input("A) Gana\nB) Egito\nC) África do Sul\nD) Uzbequistão\nE) Camarões\n\n")
    r = resposta(r)
    return r

def pergunta6():
    print("## Pergunta 6 ##")
    print("Qual cidade não pertence ao conjunto?")
    r = input("A) Londres\nB) Califórnia\nC) Buenos Aires\nD) Cidade do México\nE) Berlim\n\n")
    r = resposta(r)
    return r

def pergunta7():
    print("## Pergunta 7 ##")
    print("Qual animal não pertence ao conjunto?")
    r = input("A) Ser Humano\nB) Orangotango\nC) Cão\nD) Gorila\nE) Baleia\n\n")
    r = resposta(r)
    return r

def pergunta8():
    print("## Pergunta 8 ##")
    print("Qual seleção de futebol não pertence ao conjunto?")
    r = input("A) França\nB) Brasil\nC) Paraguai\nD) Argetina\nE) Inglaterra\n\n")
    r = resposta(r)
    return r

def minhaFase():
    pts = 0

    print("\n==== Quem é o intruso?====\n")
    print("Nesse jogo, seu objetivo é descobrir, dentre as opções, qual delas não faz parte do conjunto")
    print("Lembre-se: Você tem UMA única chance.")
    print("Por isso, pense BEM antes de responder")
    print("Bora jogar????\n")

    r = pergunta1()
    if (r == "A"):
        print("Você acertou!\n")
        pts += 1
    else:
        print("José é o único nome que não possui 4 letras e a Letra A!\n")
    
    r = pergunta2()
    if (r == "A"):
        print("Você acertou!\n")
        pts += 1
    else:
        print("Letra A é a única vogal presente nas alternativas!\n")

    r = pergunta3()
    if (r == "E"):
        print("Você acertou!\n")
        pts += 1
    else:
        print("Hulk é o único personagem listado que não é da DC Comics!\n")

    r = pergunta4()
    if (r == "D"):
        print("Você acertou!\n")
        pts += 1
    else:
        print("O número 11 é o único que não é divisível por 3!\n")

    r = pergunta5()
    if (r == "D"):
        print("Você acertou!\n")
        pts += 1
    else:
        print("Uzbequistão é o Único país que não é da África!\n")

    r = pergunta6()
    if (r == "B"):
        print("Você acertou!\n")
        pts += 1
    else:
        print("Todos são capitais de países, menos Califórnia!\n")

    r = pergunta7()
    if (r == "C"):
        print("Você acertou!\n")
        pts += 1
    else:
        print("Cão é o Único animal que não é Primata dentre as alternativas!\n")

    r = pergunta8()
    if (r == "C"):
        print("Você acertou!\n")
        pts += 1
    else:
        print("Paraguai é a única seleção dentre as alternativas que não possui uma Copa do Mundo\n")

    if (pts > 4):
        print("Você fez",pts,"pontos e ganhou!")
        time.sleep(3)
        return True
    else:
        print("Você fez",pts,"pontos e perdeu!")
        time.sleep(3)
        return False


def main():

    minhaFase()
main()



