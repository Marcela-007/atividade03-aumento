# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.

salario = float(input('Insira o valor do seu salário: '))
b = 15/100

def aumento(a,b):
    aumen = a * b
    aumentinho = aumen + salario
    print(aumentinho)

aumento(salario, b)