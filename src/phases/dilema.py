# Funcao para validar as opcoes do jogador
def optionValidator(r):
    if(r != "A" and r != "B" and r != "C" and r != "D"):
        print("Opção invlálida, tente novamente !")
        r = input("Entre com alguma das opções válidas: ").upper()
        return optionValidator(r)
    else:
        return r

def dilema1():
    print("= Dilema 1 =\n")
    print("Você está com uma faca na mão e está na casa de um desconhecido para roubar.")
    print("Você percebe que alguém da casa te viu, você vê essa pessoa correndo para dentro de um armário, o que você faz ?\n")
    r = input("A - Você sai correndo da casa\nB - Você vai até o armário finalizar a testemunha\nC - Você finje que sai da casa e espera a vitima acreditar que está tudo bem para finalizar ela\nD - Você liga para a policia para tentar inverter os papeis\nDigite a opção: ").upper()
    r = optionValidator(r)
    return r

def dilema2():
    print("\n= Dilema 2 =\n")
    print("Você está numa floresta macabra, no meio da madrugada, você sente algo atrás de você, o que você vê ?\n")
    r = input("A - Um fantasma\nB - Um animal selvagem\nC - Uma pessoa do sexo oposto\nD - Um cachorro\nDigite a opção: ").upper()
    r = optionValidator(r)
    return r

def dilema3():
    print("\n= Dilema 3 =\n")
    print("Uma pessoa esfaqueia outra pessoa dentro de um elevador, ela esfaqueia cinco vezes.")
    print("O elevador possui janelas de todos os lados.")
    print("Assim que o assassino termina de esfaquear a pessoa, ele sai do elevador e fica encarando a pessoa que foi esfaqueada")
    print("Por que ele fez isso ?")
    r = input("A - Para agir como as outras pessoas, como não soubesse o que estava acontecendo\nB - Para se deleitar com seu feito\nC - Para garantir que sua vítima estava, de fato, morta\nD - Por que ele se arrependeu\nDigite a opção: ").upper()
    r = optionValidator(r)
    return r

def dilema4():
    print("\n= Dilema 4 =\n")
    print("Você é uma garota no funeral da sua tia")
    print("E você está de luto, do seu lado, um homem muito lindo, o homem mais lindo que você viu na sua vida")
    print("E você se apaixona na hora por ele")
    print("Na próxima noita, você mata sua irmã")
    print("Por que você fez isso ?")
    r = input("A - Porque ela também era apaixonada pelo homem\nB - Porque ela era namorada dele\nC - Para ver o homem no funeral novamente\nD - O homem bonito estava apaixonado pela sua irmã\nDigite a opção: ").upper()
    r = optionValidator(r)
    return r


def dilema():
    # Pontuação geral
    points = 0

    print("\n================= Dilema (+18) =================\n")
    print("Você caminha horas, seu destino é a incrível cidade de Gluglulândia !")
    print("Todos querem chegar até lá, pelos rumores da cidade, lá é um lugar utópico.")
    print("Ninguém se atrasa, ninguém erra, ninguém esquece...")
    print("Mas para poder entrar nessa cidade, você precisa passar no teste de personalidade.")
    print("A cidade não aceita ninguém que não passe nesse teste, pois, para você entrar numa cidade perfeita, você precisa ser perfeito.\n")

    print("Quando você chega nos guardas, eles fazem diversas perguntas\n")

    r = dilema1()
    if(r == "C"):
        points -= 3

    r = dilema2()
    if(r == "D"):
        points -= 3
    else:
        points += 1

    r = dilema3()
    if(r == "A"):
        points -= 3
    elif(r == "D"):
        points += 3
    
    r = dilema4()
    if(r == "C"):
        points -= 3
    
    if(points == -12):
        print("Amigo, você precisa de ajuda, você tem tendências psicopatas.\n")
        return False
    
    elif(points == 4):
        print("Parabéns, você possui um bom coração, pode entrar em nossa cidade.\n")
        return True
    
    elif(points >= 0 and points < 4):
        print("Você não foi tão mal nos questionários, vamos deixar você ficar temporáriamente em nossa cidade.\n")
        return True
    
    else:
        print("Você não passou nos testes. Não é bem vindo em nossa cidade.\n")
        return False