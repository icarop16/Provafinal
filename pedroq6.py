positivos = 0 #Quantidade de números positivos
Lista = [] #Aqui sera adicionado os números positivos, acrescentaremos eles nesta lista

for i in range (6): #Estrutura de repetição 
    n = float(input(f"Digite o {i + 1}° número de sua lista:")) #inserir os números na lista
    if n > 0: #Caso o número for maior que 0, será positivo
        positivos +=1 #Acrescenta um valor ao número positivo
        Lista.append(n) #Acrescenta o número á lista
soma = sum(Lista) #soma a lista
media = soma /positivos #calcula á media dos números positivos
print ("Você digitou %d números positivos"%positivos) #quantidade de números positivos
print (f"{media}") #Media de números positivos