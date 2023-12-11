renda = float(input("Digite ao lado o valor da sua renda atual: ")) #Aqui sera adicionado o valor da renda

if renda <= 2000.00: # Calcula o imposto até 2000.00
    print("Isento")

elif renda == 2000.01 or renda <= 3000.00: #Calcula o imposto de 2000.01 até 3000.00
    print ("O imposto da sua renda é de 8%.")
    imposto = (renda * 8)/100
    print(f"{imposto:.2f}")

elif renda == 3000.01 or renda <= 4500.00: #Calcula o imposto de 3000.01 até 4500.00
    print("O imposto da sua renda é de 18%.")
    imposto2 = (renda * 18)/100
    print(f"{imposto2:.2f}")

else: #Calcula o imposto até 4500.00
    print("O imposto da sua renda é de 28%.")
    imposto3 = (renda * 28)/100
    print(f"{imposto3:.2f}")