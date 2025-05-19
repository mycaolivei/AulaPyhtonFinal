with open("Nomes.txt", "a") as arquivo:
    nome=input("Digite o seu nome: ")
    arquivo.write(f"{nome} \n")