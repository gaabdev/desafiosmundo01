#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input("Digite o seu salário: "))

novo = salario + (salario *15/100)
print("O funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salario, novo))


# Para se inserir a formatação de números em casas decimais, primeiro é necessário  adicionar os dois pontos junto ao ponto e 
# adicionar o número que será dado de casas com f de formatar