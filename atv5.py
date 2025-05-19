try:
    idade=int(input("Digite a sua idade: "))
    idade.append()
except AttributeError:
    print("Você está tentando atribuir um metodo a uma string")