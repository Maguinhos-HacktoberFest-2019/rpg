#  Hacktober Fest Manguinhos - 2019
#  Rafaela Amorim Pessin

import time
from random import randint

def caraCoroa():
	
	print("Olá, jovem gafanhoto!")
	time.sleep(1)
	print("Chegou a hora de testar sua sorte...")
	time.sleep(2)
	print("Agora nós vamos jogar Cara ou Coroa!")
	time.sleep(2)
	print("Voce tem 20 chances... Preparado?")
	time.sleep(2)
	
	x = 0; jogador = 0; computador = 0; i = 0
	print("\nEscolha 0 se você quer CARA ou escolha 1 se você quer COROA...")
	while (i < 20):
		x = int(input("\nCara ou Coroa? "))
		while (x!=1 and x!=0):
			x = int(input("\nCara ou Coroa? "))
			
		y = randint(0, 1)
		
		if (x == y):
			jogador = jogador+1
		else:
			computador = computador+1
			
		i+=1
			
	if (jogador > computador):
		print("Pontuacao:", jogador)
		print("\o/ \o/ \o/ PARABENS! VOCE GANHOU!!!!! \o/ \o/ \o/")
		return True
		
	if (jogador == computador):
		print("Pontuacao:", jogador)
		print("Houve empate! =O")
		return False
		
	else:
		print("Pontuacao:", jogador)
		print(")= Que pena, nao foi dessa vez! =(")		
		return False
