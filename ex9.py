peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Peso abaixo do normal.")
elif imc <= 24.9:
    print("Peso normal.")
elif imc <= 29.9:
    print("Sobrepeso.")
elif imc <= 34.9:
    print("Obesidade grau I.")
elif imc <= 39.9:
    print("Obesidade grau II.")
else:
    print("Obesidade grau III.")
print("IMC:", imc)