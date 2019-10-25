from random import randint
from phases.start import start
from phases.hangman import hangman
from phases.dilema import dilema
from phases.velha import velha
from phases.forca import forca

g_phases = [forca, start, dilema, velha, hangman]

class Settings():
    hardcore = False
    
    def __init__(self):
        self.config()
    #
    
    def config(self):
        #TODO: coletar configurações do usuário
        pass
    #
#

class Player():
    name = "Youngling"
    isAlive = True
    
    def __init__(self, settings=Settings()):
        self.settings = settings
        self.name = input("Nos diga qual seu nome de jogador!\n")
    #
#

def play(id):
    phase = g_phases[id]
    result = phase()
    
    if result:
        g_phases.pop(id)
    #
    
    return result
#

def runGame(player):
    play(0)

    # Engine
    while len(g_phases) > 0:
        phaseId = randint(0, len(g_phases)-1)
        phaseResult = play(phaseId)
        
        if player.settings.hardcore and not phaseResult:
            print("Você perdeu =/")
            break
        #
        
        while not phaseResult:
            res = input("Você perdeu, quer tentar novamente? (s/n): ")
            if res.lower() == "s":
                phaseResult = play(phaseId)
            else:
                phaseResult = True
            #
        #
    #

    print("Game over...")
#

def main():
    print("Olá, player. Bem vindo ao Random RPG. Vamos começar?")
    player = Player()
    runGame(player)
#

if __name__ == "__main__":
    main()
#
