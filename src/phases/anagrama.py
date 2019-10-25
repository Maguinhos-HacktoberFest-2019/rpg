import sys

def anagrama1():
    print("SERA => _ _ _S")
    resposta = input("Digite a palavra escondia: ").upper()
    return resposta



def verificaResposta(resposta):
    if resposta.upper() == "ERAS":
        return True
    else:
        return False
        


def anagrama():
    print("Descubra qual é a palavra que está escondida em cada uma das palavras bagunçadas")
    resp = anagrama1()
    print(resp.upper())
    if verificaResposta(resp): 
        print("Parabéns !!! Você acertou")
        return True
    else:
        print("Resposta ERRADA !!!")
        return False
print("top")

anagrama()
