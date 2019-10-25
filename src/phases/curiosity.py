# Autor: Brian Icaro
def optionValidator(r):
    if(r != True and r!= False):
        print("Opção inválida, tente novamente!");
        r = input("Entre com alguma das opções válidas")
        return optionValidator(r)
    else:
        return r

def curiosidade1():
    print("Curiosidade 1:\n")
    print("É verdade que Leite de hipopótamo é rosa?")
    r = input("True: Verdadeiro\n False: Falso\n")
    r = optionValidator(r)
    return r


def curiosidade():
    r = curiosidade1()
    if(r == 'True'):
        print('Parabéns, você detem conhecimento muito útil!')
    else:
        print('Bom, ao menos isso não cai em prova de concurso.')


    return True
#