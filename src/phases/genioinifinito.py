#autor: Felipe Becalli Trindade

def abacate(x):
	j = input("\n**TABELA ASCII**\nBinário: 00100000: ")
	y = " "
	if x == 6:	
		if j.lower() != y.lower():
			print('\nVocê não é de pedra. Você ainda tem {} chances'.format(x-1))
			abacate(5)
		else:
			return True
	elif x == 5:
		if j.lower() != y.lower():
			print('\nVeja direito o código. Você ainda tem {} chances'.format(x-1))
			abacate(4)
		else:
			return True
	elif x == 4:
		if j.lower() != y.lower():
			print('\nCara, Como assim?. Você ainda tem {} chances'.format(x-1))
			abacate(3)
		else:
			return True
	if x == 3:	
		if j.lower() != y.lower():
			print('\nNão sabe seguir ordens? Você ainda tem {} chances'.format(x-1))
			abacate(2)
		else:
			return True
	elif x == 2:
		if j.lower() != y.lower():
			print('\nOlhe a tabela ASCII e traduza o Binário para ASCII... Você ainda tem {} chances'.format(x-1))
			abacate(1)   
		else:
			return True
	elif x == 1:
		if j.lower() != y.lower():
			print('\nVocê perdeu!')
			return False
		else:
			print("Até que enfim, o GÊNIO NÃO QUER MAIS VOCÊ POR PERTO, ELE VAI SER CHATO COM OUTRO!")
			return True

def pure(x):
	j ='Resposta'
	resp1=input("\nDigite Resposta: ")
	if resp1.lower() != j.lower():
		print('\nResposta é errada!\nVocê ainda tem 5 chances')
		resp2=input("\nDigite a Resposta: ")
		if resp2.lower() != x.lower():
			print('\nSério? \nVocê ainda tem 4 chances')
			resp3=input("\nDigite a Resposta: ")
			if resp3.lower() != x.lower():
				print('\nVai, vai, se errar novamente eu te dou uma dica!\nVocê ainda tem 3 chances')
				resp4=input('\nDigite a Resposta: ')
				if resp4.lower() != x.lower():
					print('\nVolte atrás, ela está explicíta\nVocê ainda tem 2 chances')
					resp5=input('\nDigite a Resposta: ')
					if resp5.lower() != x.lower():
						print('\nDESISTO DE VOCÊ!\nVocê tem 1 chance!')
						resp6=input('\nDigite a Resposta: ')
						if resp6.lower() != x.lower():
							print('\nO GÊNIO TE APRISIONOU NO INFINITO!')
							return False
						else:
							print("\nParábens você sabe escrever a resposta")
							abacate(1)
					else:
						print("\nParábens você sabe escrever a resposta")
						abacate(2)
				else:
					print("\nParábens você sabe escrever a resposta")
					abacate(3)
			else:
				print("\nParábens você sabe escrever a resposta")
				abacate(4)
		else:
			print("\nParábens você sabe escrever a resposta")
			abacate(5)
	else:
		print("\nParábens você sabe escrever a Resposta")
		abacate(6)

def fasegenius():
	respdo1='errada' #Resposta do 1 input
#   INTRODUÇÃO DO GAME
	print('\nUM GÊNIO MANDÃO DISSE PARA SEGUIR SUAS ORDENS. E RESPONDER TRÊS PERGUNTAS PARA ELE! VOCÊ SE ACHA INTELIGENTE PARA PASSAR NO DESAFIO?')
	xx='"B A N A N A"'
	print("\nVocê sabe escrever  {} ?\nVocê tem 6 chances no total".format(xx))
# fim introdução
	return pure(respdo1)
fasegenius()