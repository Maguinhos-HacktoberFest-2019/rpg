from time import sleep
from random import randint
def alex_kid():
    lista = ["PAPEL","PEDRA","TESOLRA"]
    boss = randint(0,2)
    print(''' FAÇA  SUA ESCOLHA
            [0]PAPEL
            [1]PEDRA
            [2]TESOLRA''')
    alex = int(input("Faça  sua escolha: "))
    print(f"BOSS ESCOLHEU: {lista[boss]}")
    print(f"ALEX ESCOLHEOU: {lista[alex]}")
    return True

alex_kid()