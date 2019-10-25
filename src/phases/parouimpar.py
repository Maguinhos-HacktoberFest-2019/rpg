#Criado por Felipe Gante

from random import randint

def parouimpar():
    pc = randint(0, 9)
    escolha = int(input('Escolha ímpar(1) ou par(2)?')
    print('PROCESSADO...')
    jogador = int(input('Escolha um número:')
    print('Você escolheu o número {} e Eu o número {} !'.format(escolha, pc))
    if escolha == 2:
        if ((pc+jogador)%2 == 0):
            print('PARABÉNS! Você conseguiu me vencer!')
            return True
        else:
            print('GANHEI! Nunca me ganharam nesse jogo')
            return False
    else:
        if ((pc+jogador)%2 == 0):
            print('GANHEI! Nunca me ganharam nesse jogo')
            return False
        else:
            print('PARABÉNS! Você conseguiu me vencer!')            
            return True