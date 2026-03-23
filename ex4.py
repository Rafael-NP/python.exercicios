# Faça um programa que gere o preço de um veículo para o cosumidor final com os impostos e o lucro do distribuidor (impostos = 45%, lucro = 12%).

valor = float(input("Digite o valor incial: "))
print("Valor com impostos:", valor + valor *0.45)
print("Lucro:", valor * 0.12)