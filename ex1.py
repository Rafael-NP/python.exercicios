# Crie um programa que solicite o valor de compra e informe ao cliente se terá desconto (valor > 100).

valor = float(input("Digite o valor da compra: "))
if valor > 100.00:
    print("Você terá desconto!")
else:
    print("Sem desconto.")