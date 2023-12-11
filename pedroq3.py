senha = 1 # Senha  do Usuario
while senha != 2002: #Compara a senha fixa com a tentativa de senha ate o usuario colocar a certa 
    print ("Adicione a senha correta:") # Pede a senha para o usuario 
    senha = int(input())
    if senha != 2002: #Se for uma senha diferente, mostra "Senha invalida"
        print("Senha Invalida")
    else: #Se for igual mostra "Acesso Permitido"
        print("Acesso Permitido")
        break #Encerra o while 