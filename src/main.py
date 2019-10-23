from random import randint

from phases.start import start
from phases.hangman import hangman
from phases.dilema import dilema

g_phases = [start, dilema]

class Player():
    name = "Youngling"
    isAlive = True
    
    def __init__(self, settings):
        self.settings = settings
        self.name = "Youngling" #TODO: Pegar nome pelo prompt
    #
#

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

def play(id):
    phase = g_phases[id]
    result = phase()
    
    if result:
        g_phases.pop(id)
    #
    
    return result
#

def runGame(player):    
    # Engine
    while len(g_phases) > 0:
        phaseId = randint(0, len(g_phases)-1)
        phaseResult = play(phaseId)
        
        if player.settings.hardcore and not phaseResult:
            print("Você perdeu! Inicie o jogo novamente.")
            break
        #
        
        while not phaseResult:
            print("Tente novamente!")
            phaseResult = play(phaseId)
        #
    #
#

def main():
    # TODO: Adicionar mensagem de boas vindas!
    settings = Settings()
    player = Player(settings)
    runGame(player)
#

if __name__ == "__main__":
    main()
#
