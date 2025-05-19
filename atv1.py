nome= 'print("Digite o seu nome: )'
try:
    exec(nome)
except SyntaxError:
    print(" você está tentando operação a uma string")

