contador = 0 #Variavel inicial
print ("Digite cinco valores inteiro:")
for i in range (1, 6): #Estrutura de repetição
    n = int(input()) #Pede que o usuario insira 5 números
    if n % 2 == 0:# Calculo de número par. Se o reto da divisão por dois for zero, a condição é verdadeira 
        contador +=1 # Caso a condição acima seja verdadeira, o programa acrescentará +1 na variavel "contador"
print ("Você digitou %d valores pares"%contador) #Retornara a quantidade armazenada na variavel "Contador"