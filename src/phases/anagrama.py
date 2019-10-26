import sys

def anagrama1():
    print("SERA => _ _ _ S")
    resposta = input("Digite a palavra escondia: ").upper()
    return resposta


def anagrama2():
    print("ÁTIX => T _ _ _")
    resposta = input("Digite a palavra escondia: ").upper()
    return resposta


def anagrama3():
    print("ALAF => F _ _ _")
    resposta = input("Digite a palavra escondia: ").upper()
    return resposta


def anagrama4():
    print("ÓCISP => _ _ _ Ó _")
    resposta = input("Digite a palavra escondia: ").upper()
    return resposta


def anagrama5():
    print("OSTEP => _ _ _ _ E")
    resposta = input("Digite a palavra escondia: ").upper()
    return resposta


def anagrama6():
    print("MARAR => _ A _ _ _")
    resposta = input("Digite a palavra escondia: ").upper()
    return resposta


def anagrama7():
    print("TLAROS => _ O _ _ A _")
    resposta = input("Digite a palavra escondia: ").upper()
    return resposta

def anagrama8():
    print("PETASO => _ _ _ O _ A")
    resposta = input("Digite a palavra escondia: ").upper()
    return resposta

def anagrama9():
    print("ÔINONAM => A _ Ô _ _ M _")
    resposta = input("Digite a palavra escondia: ").upper()
    return resposta

def anagrama10():
    print("PRICOEMÍ => _ M P _ _ I _ _")
    resposta = input("Digite a palavra escondia: ").upper()
    return resposta

def verificaResposta(resposta):
    pontos = 0
    if resposta.upper() == "ERAS":
        pontos += 3
        print("Resposta CERTA!!!\n")
        return pontos
    elif resposta.upper() == "TÁXI":
        pontos += 3
        print("Resposta CERTA!!!\n")
        return pontos
    elif resposta.upper() == "FALA":
        pontos += 3
        print("Resposta CERTA!!!\n")
        return pontos
    elif resposta.upper() == "CIPÓS":
        pontos += 3
        print("Resposta CERTA!!!\n")
        return pontos
    elif resposta.upper() == "MARRA":
        pontos += 3
        print("Resposta CERTA!!!\n")
        return pontos
    elif resposta.upper() == "POSTE":
        pontos += 3
        print("Resposta CERTA!!!\n")
        return pontos
    elif resposta.upper() == "SOLTAR":
        pontos += 3
        print("Resposta CERTA!!!\n")
        return pontos
    elif resposta.upper() == "ESTOPA":
        pontos += 3
        print("Resposta CERTA!!!\n")
        return pontos
    elif resposta.upper() == "ANÔNIMO":
        pontos += 3
        print("Resposta CERTA!!!\n")
        return pontos
    elif resposta.upper() == "EMPÍRICO":
        pontos += 3
        print("Resposta CERTA!!!\n")
        return pontos
    else:
        pontos -= 3
        print("Resposta ERRADA !!!\n")
        return pontos
        


def anagrama():
    print("Descubra qual é a palavra que está escondida em cada uma das palavras bagunçadas")
    print("Para passar essa fase precisa acertar no mínimo 12 pontos")
    print("Cada palavra CERTA você acumula 3 pontos")
    print("E para cada palavra ERRADA são retidados 3 pontos\n")

    pontos = 0 
    pontos += verificaResposta(anagrama1())
    pontos += verificaResposta(anagrama2())
    pontos += verificaResposta(anagrama3())
    pontos += verificaResposta(anagrama4())
    pontos += verificaResposta(anagrama5())
    pontos += verificaResposta(anagrama6())
    pontos += verificaResposta(anagrama7())
    pontos += verificaResposta(anagrama8())
    pontos += verificaResposta(anagrama9())
    pontos += verificaResposta(anagrama10())
    
    if pontos >= 12 :
        print("\nParabéns!!! Você concluiu a fase do jogo. Você acertou ", pontos," pontos")
        return True
    elif pontos< 12:
        print("\nDesculpe, não foi desse vez. Você acertou ",pontos," pontos")
        return False


