
def resposta(r):
	if (r==4):
		result=True
		print('Lula está te esperando no presidio. Vá em frente!')
	else:
		result=False
		print('Não foi dessa vez , jovem. tente de novo!')
	return result

def enigma1(args):
	print('Você entra numa sala escura. \nNo quarto há uma estufa a gás, uma luminária de querosene e uma a vela.\
	\nTem uma caixa de fósforos com um só fósforo em seu bolso\
	\nQual você ascende primeiro? ')
	print('1 - Estufa de gás \n2- Luminária(guerosene) \n3- Luminária(a vela) \n4- Nenhum das alternativas')
	r=input('Qual sua resposta?(1, 2, 3, 4)  \n')
	ver=resposta(r)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(enigma1(sys.argv))
