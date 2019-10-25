
def resposta(r):
	if (r=='PESSOA')or (r=='SER HUMANO')or(r=='HOMEM')or (r=='HUMANO'):
		result=True
		print('Lula está te esperando no presidio. Vá em frente!')
	else:
		result=False
		print('Não foi dessa vez , jovem. tente de novo!')
	return result

def main(args):
	print(' O que caminha com quatro pernas pela manhã,duas pernas ao meio-dia e três pernas à noite?')
	r=input('Sua resposta: ').upper()
	ver=resposta(r)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
