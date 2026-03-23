# Faça um programa que solicite 5 números, calcule e apresente a soma total

i = 1
soma = 0
while i < 6:
    num = float(input("Digite um número: "))
    soma += num
    i += 1
print("A soma é:", soma)