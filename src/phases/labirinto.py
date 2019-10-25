def labirinto():
    print("Você acorda perdido em um labirinto, na sua frente tem dois caminhos, um claro e um escuro, qual você vai seguir?\n")
    r = input("Resposta (claro ou escuro): ").lower()
    if r == "claro":
        print("a claridade vinha de armadilhas com fogo que te mataram...")
        return False
    else:
        print("O caminho deu em um sala, no fim da sala há uma porta suja de sangue, você vai abrir a porta ou voltar?")
        r = input("Resposta (abrir ou voltar): ").lower()
        if r == "voltar":
            print("Ao voltar uma armadilha na porta te matou")
            return False
        else:
            print("A porta levava a um corredor, nesse corredor tem uma escada e um porão, por qual caminho você quer seguirw")
            r = input("Resposta (escada ou porao): ").lower()
            if r == "escada":
                print("A escada dava até a saida do labirinto, com sorte ele era bem curto não é mesmo?")
                return True
            else:
                print("O porão não tinha fundo, você escorregou e caiu de uma altura muito grande")
                return False
                
            
            
