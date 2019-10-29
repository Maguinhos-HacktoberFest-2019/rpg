#Autor: Joao Pedro Garcia Pereira
def escolhas():
	def validador(resposta):
		while resposta!=1 and resposta !=2:
			print("Esta não é uma resposta válida, tente novamente")
			resposta=int(input("Oque você deseja? (1 ou 2): "))
		return resposta
	gameover=4
	restart=1
	while restart==1 and gameover>0:
		restart=0
		gameover=gameover-1
		print("Após uma longa jornada de aventura... \n")
		print("você (como um bom aventureiro programador), resolve ir tomar um café")
		print("Enquanto caminhava você observa pessoas mascaradas saindo da cafeteria...\n")
		print("É UM ASSALTO!!!\n")
		print("Essa não, os assaltantes mascarados roubaram todos os sacos de café! Oque deseja fazer? (1 ou 2)\n\n\n")
		print("Correr atrás dos assaltantes (Alguem que rouba café não pode sair impune) (1)		Ir em uma outra cafeteria (2)\n")
		resposta=int(input())
		resposta=validador(resposta)
		if resposta==2:
			print("Aparentemente aquela não era a única cafeteria que foi roubada, todas estão sem café")
			print("Você ficou sem café e todo mundo sabe que não é possível programar sem café\n\n\n")
			print("GAME OVER\n\n")
			restart=int(input("Digite 1 para tentar novamente! %d tentativas restantes: "%gameover))
		else:
			print("Por algum motivo o seu instinto de amante de café, faz você correr atrás dos mascarados")
			print("Enquanto corria você vê um menino com uma bicicleta. O que deseja fazer? (1 ou 2)\n\n\n")
			print("Roubar a bicicleta (afinal tudo por CAFÉ) (1)    Continuar correndo (2)" )
			resposta=int(input())
			resposta=validador(resposta)
			if resposta==1:
				print("Você rouba a bicicleta e consegue atropelar um dos assaltantes")
				print("Porém aquele menino era filho de um policial, que conseguiu chegar até você\n")
				print("VOCÊ ESTÁ PRESO!!!")
				print("...\n")
				print("........\n")
				print("............................................\n")
				print("Você está preso mas tem seu precioso cafe, então considere uma vitória!!")
			else:
				print("Você continua correndo até que um dos assaltantes acaba deixando cair um saco")
				print("Você leva de volta para a cafeteria, todos te chamam de herói e ganham uma rodada grátis de café!!\n\n")
				print("BIG WIN!")
	if gameover<0:
		return False
	else:
		return True
