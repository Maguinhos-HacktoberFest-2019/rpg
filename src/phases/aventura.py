def aventura():
    acao = ''
    grito = ''
    nome = ''
    
    print('Você esta de olhos fechados. Não sente sua cama, todas as sensações que seu corpo lhe devolve é a sensação de estar deitado na areia molhada.')
    print('Não esta no conforto da sua cama. Não sente seu travesseiro.')
    print('"Aonde estou?" - Você se pergunta. Mas é impossível saber sem abrir os olhos. O que você fará?')
    acao = input('Digite a ação "abrir os olhos".\n')
    while acao != 'abrir os olhos':
        acao = input('Você não abriu os olhos ainda. Digite a ação abrir os olhos para continuar.')
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
    print('Entendo, caro %s')

    return True

if __name__ == '__main__':
    import sys
    sys.exit(aventura())
