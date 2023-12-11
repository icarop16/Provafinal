print("Adicione o DDD para qual você deseja discar: ") #Pergunta qual DDD que o usuario deseja.
Numero = int(input(""))
def ddd(): #Compara o ddd discado com a "biblioteca" de dados do programa.
    if Numero == 61:#Caso o número estiver na biblioteca, ira aparecer a cidade correspondente.
        print("Brasilia")
    elif Numero == 71:
        print("Salvador")
    elif Numero == 11:
        print("São Paulo")
    elif Numero == 21:
        print("Rio de Janeiro")
    elif Numero == 32:
        print("Juiz de Fora")
    elif Numero == 19:
        print("Campinas")
    elif Numero == 27:
        print("Vitoria")
    elif Numero == 31:
        print("Belo Horizonte")
    else:
        print("DDD não cadastrado.")##Caso o número não estiver na biblioteca, ira aparecer "DDD não cadastrado".
ddd() #Retorna a função.
        