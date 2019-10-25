def verifica_resposta(chances, resp):
	if chances > 0 and (resp < 7.5 or resp > 12.5):
		resp = float(input('Voce so tem mais uma chance, nao à disperdice: '))
		verifica_resposta(0, resp)
		
	else:
		if resp >= 7.5 and resp <= 12.5:
			print('Dilma mandou dizer que voce é um genio!')
			return True
		else:
			print('\n\n----------------------GAME OVER------------------------------')
			return False

def startgame():
	print('\nAcredite... É um texto\n')
	print('4E 61 6F 20 65 20 33 30 25 20 \n64 6F 73 20 72 65 63 75 72 73 \n6F 73 20 64 61 20 65 78 70 6C \n6F \
72 61 E7 E3 6F 2E 20 45 20 \n33 30 25 20 64 65 20 32 35 20 \n25 2E 20 4F 75 20 33 30 25 2E \n2E 2E 5C 6E 64 \
65 33 30 25 2E \n20 50 6F 72 74 61 6E 74 6F 2C \n20 6E 61 6F 20 65 20 33 30 25 \n2E')
	
	resp = input('\nDica: a resposta é um float\n\nEntao esta entre? ')
	
	while not resp.isnumeric():
		resp = input('Disse que a resposta era um float meu consagrado ;)\nTente novamente: ')
	
	verifica_resposta(1, float(resp))

def enigma_hex():
	print('ARE YOU READYYYYYY?!')
	a = input('Pressione enter para continuar...')
	
	while a != '':
		a = input('Voce consegue ;)\nPressione enter para continuar...')
	
	print('\n---------------------------------BOA SORTE-----------------------------------\n')
	print('-------------------------------Fase: ENIMIGA.HEX-------------------------------')
	startgame()

if __name__ == '__main__':
	enigma_hex()
