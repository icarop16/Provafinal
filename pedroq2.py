salário = float(input("Digite o valor do seu salário: ")) #Aqui sera adicionado o valor do salário do funcionario.

if salário <= 400.00: #Aqui vai fazer o calculo do aumento do funcionários
    reajuste = (salário * 15)/100
    novoS = (salário + reajuste)
    print(f"""Novo salario: {novoS:.2f}
Reajuste ganho: {reajuste:.2f}
Em Percentual: 15%""")

elif salário == 400.01 or salário <= 800.00: #Aqui vai fazer o calculo do aumento do funcionários
   reajuste2 = (salário * 12)/100
   novoS2 = (salário + reajuste2)
   print(f"""Novo salario: {novoS2:.2f}
Reajuste ganho: {reajuste2:.2f}
Em Percentual: 12%""")

elif salário == 800.01 or salário <= 1200.00: #Aqui vai fazer o calculo do aumento do funcionários
   reajuste3 = (salário * 10)/100
   novoS3 = (salário + reajuste3)
   print(f"""Novo salario: {novoS3:.2f}
Reajuste ganho: {reajuste3:.2f}
Em Percentual: 10%""")
   
elif salário == 1200.01 or salário <= 2000.00: #Aqui vai fazer o calculo do aumento do funcionários
   reajuste4 = (salário * 7)/100
   novoS4 = (salário + reajuste4)
   print(f"""Novo salario: {novoS4:.2f}
Reajuste ganho: {reajuste4:.2f}
Em Percentual: 7%""")


else: #Calcula o aumento do funcionario
   reajuste5 = (salário * 4)/100
   novoS5 = (salário + reajuste5)
   print(f"""Novo salario: {novoS5:.2f}
Reajuste ganho: {reajuste5:.2f}
Em Percentual: 4%""")