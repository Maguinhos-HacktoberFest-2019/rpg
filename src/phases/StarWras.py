
def resposta(r):
	if (r=='V'):
		result=True
		print('Lula está te esperando no presidio. Vá em frente!')
	else:
		result=False
		print('Não foi dessa vez , jovem. tente de novo!')
	return result


def Starwars(args):
	
	print(' #Barulho- \n\
	Verdadeiro ou Falso:\n \
	Se houvesse guerras no espaço, como no filme Guerra nas Estrelas (Star Wars) ,\n \
	o barulho de tiros e perseguições não seriam ouvidos \n')
	
	r=input('Qual sua resposta?(V/F) ').upper()
	ver=resposta(r)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(Starwars(sys.argv))
