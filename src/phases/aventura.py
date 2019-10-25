import time
def aventura():
	acao = ''
	grito = ''
	nome = ''
	q1 = ''; q2 = ''; q3 = ''
	
	print('Você esta de olhos fechados. Não sente sua cama, todas as sensações que seu corpo lhe devolve é a sensação de estar deitado na areia molhada.')
	print('Não esta no conforto da sua cama. Não sente seu travesseiro.')
	print('"Aonde estou?" - Você se pergunta. Mas é impossível saber sem abrir os olhos. O que você fará?')
	acao = input('Digite a ação "abrir os olhos".\n')
	while acao != 'abrir os olhos':
		acao = input('Você não abriu os olhos ainda. Digite a ação abrir os olhos para continuar.\n')
	print('Você abre os olhos e começa a observar o que esta a sua volta. Tudo o que vê é um bosque.')
	print('"Uma floresta... Tropical?" - Você se pergunta. Mas nunca foi muito bom em reconhecer os biomas.')
	print('Tenta pensar no que fazer, mas nada lhe passa pela sua mente. Contudo, sem que percebesse, começa a andar pela floresta.')
	print('Não se passa muito tempo até que percebe que esta andando sozinho. Sem querer. Como se algo lhe puxasse.')
	print('"Que diabos? Como paro?" - Você gritava, em desespero completo.')
	print('Tudo que se lembrava do dia anterior, era de ter ido dormir. Então por que estava ali? O pânico toma conta de ti, então começa a gritar mais alto.')
	grito = input('O que você esta gritando?\n')
	print('%s não muda nada.' %(grito))
	grito = input('O que você esta gritando?\n')
	print('Mas gritar %s não trás ninguém para te salvar.' %(grito))
	print('Você esta tremendo e suando muito. Mas nada muda. Até que um precipicio aparece em sua frente.')
	print('Quando você avista o precipicio, suas pernas começam a correr. Você se debate, mas nada muda. Até que para, a três passos do precipicio.')
	print('Uma risada aterrorizante ecoa do fundo do precipicio. E você assustado, grita de volta, em pânico.')
	nome = input('"Qual o seu nome, meu caro?" - Pergunta a voz. Curiosa sobre quem estaria ali.\n')
	print('"Entendo, caro %s. No entanto, no momento, você esta sob meu controle. Responda uma das três perguntas corretamente e eu te retornarei para o conforto se sua casa."' %(nome))
	print('"Do contrário, passará o resto da eternidade comigo. Aqui. E eu lhe asseguro, não sou uma companhia agradável." - A voz gargalha.')
	print('Enquanto a voz falava, era possível ouvir os sons de correntes e de carne sendo mastigada.')
	print('"Então, vamos começar?" - Perguntava a voz, maliciosamente.')
	q1 = input("Se eu voltase no tempo, e por acaso matasse meu pai antes dele conhecer minha mãe. O que aconteceria?\n")
	print('A voz gargalha e zomba de ti. "Não existe resposta certa para essa pergunta. Esta mais próximo de mim."')
	q2 = input("Se um ser onipotente é capaz de criar qualquer coisa, então ele seria capaz de criar uma pedra tão pesada que nem mesmo ele seria capaz de erguer?\n")
	print('A voz novamente ri. Uma risada fria. Sádica. Ela claramente estava apenas jogando com você. Ela pretendia apenas se divertir contigo antes de finalmente lhe matar?')
	print('Seu corpo treme. Você começa a suar tanto que têm a sensação de que um rio esta saindo do seu corpo. É ridiculo. Seria melhor desistir.')
	print('Você faz gritos de protestos. Aparentemente, a voz resolve lhe dar uma chance, e faz a última pergunta.')
	q3 = input('"Se todo dia você toma banho e sai limpo, por que toda semana tem que colocar a toalha para lavar?"\n "Irei facilitar para você. Você tem três opções."\n 1 - Porque as bactérias sujam a toalha.\n 2 - Por coerção social. A toalha esta sempre limpa e o fedor dela é alucinação coletiva.\n 3 - Foda-se, vadia, puta. Ninguém liga. \n')
	if q3 == '1':
		print('"Dessa vez, você se safou, %s. Da próxima, não serei tão bonzinho. Lhe espero em seus sonhos." - A voz ri sádicamente e o cenário se desvai, com você voltando para seu quarto e despertando em sua cama.' %(nome))
		time.sleep(3)
		return True
	else:
		print('Seu corpo é levado a dar mais um passo. Você então começa a cair. Tenta gritar. Mas a voz não sai.')
		print('Enquanto cai, você vai perdendo a consciência lentamente. Completamente em pânico, sua última visão são dois brilhos vermelhos. Como se fossem olhos, no fundo do abismo, aguardando sua descida.')
		time.sleep(6)
		return False

if __name__ == '__main__':
	import sys
	sys.exit(aventura())
