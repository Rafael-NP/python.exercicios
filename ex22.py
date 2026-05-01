try:
    valor = float(input("Digite o valor: "))
    qtd = int(input("Digite a quantidade: "))
    valorFinal = valor * qtd
    print("O valor final é:", valorFinal)
except:
    print("Valor ou quantidade inválido.")