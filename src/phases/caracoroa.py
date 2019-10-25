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
	print("Você tem 10 chances... Preparado?")
	time.sleep(2)
	
	x = 0; jogador = 0; computador = 0; i = 0
	print("\nEscolha 0 se você quer CARA ou escolha 1 se você quer COROA...")
	while (i < 10):
		x = int(input("\nCara ou Coroa? "))
		#adicionar um while
		y = randint(0, 1)
		
		if (x == y):
			jogador = jogador+1
		else:
			computador = computador+1
			
		i+=1
			
	if (jogador > computador):
		print("Pontuação", jogador)
		print("\o/ \o/ \o/ PARABÉNS! VOCÊ GANHOU!!!!! \o/ \o/ \o/")
		return True
		
	if (jogador == computador):
		print("Pontuação", jogador)
		print("Houve empate! =O")
		return False
		
	else:
		print("Pontuação", jogador)
		print(")= Que pena, não foi dessa vez! =(")		
		return False

def main(args):
	
	caraCoroa()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
