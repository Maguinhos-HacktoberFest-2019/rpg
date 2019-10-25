from random import randint
from phases.start import start
from phases.hangman import hangman
from phases.dilema import dilema
from phases.velha import velha
from phases.caracoroa import caraCoroa
from phases.alexkid import alex_kid
from phases.labirinto import labirinto
from phases.charada import charada
from phases.enigma_hex import enigma_hex
from phases.portas import postas
from phases.respiro import respiro
from phases.vocemorreu import morreu
from phases.curiosity import curiosidade
from phases.jogosequencia import jogosequencia
g_phases = [start, dilema, velha, hangman, curiosidade, jogosequencia, postas, enigma_hex]

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
