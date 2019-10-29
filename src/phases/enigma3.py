
def resposta(r):
	if (r=='eu')or(r=='eu sou o piloto')or(r=='eu sou')or (r=='eu mesmo'):
		result=True
		print('Lula está te esperando no presidio. Vá em frente!')
	else:
		result=False
		print('Não foi dessa vez , jovem. tente de novo!')
	return result

def main(args):
	print(' Você é um piloto de avião que voa de londres a Berlin, com duas escalas em Praga. \nComo o piloto se chama?')
	r=input('Sua resposta: ').lower()
	ver=resposta(r)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
