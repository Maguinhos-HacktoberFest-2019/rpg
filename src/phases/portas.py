#Autor : Thiago da Costa Freitas

def postas():
    porta=0
    print("Ao final do corredor, se depara com duas portas. Uma a esquerda e outra a direita. Balrog está atrás de você")
    print("Você não sabe o que lhe encontra atrás de cada porta. Mas sabe que se ficar parado, ou voltar, irá morrer")
    print("Escolha uma e sobreviva... ou morra")
    porta=int(input("1 para a porta da esquerda ou 2 para a porta da direita"))
    if porta == 1:
        print("Você sobreviveu, continue correndo do Balrog!")
        return True
    if porta == 2:
        print("As vezes a vida não é justa, outro Balrog atrás dessa porta. Você morreu")
        return False
    if porta != 1 and porta !=2:
        print("Não escolheu nenhuma das portas? Balrog te pegou. Tu morreu.")
        return False


