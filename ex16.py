def calc_valor(a,b):
    valor = a * b
    return valor
preco = float(input("Digite o preço unitário: "))
qtd = int(input("Digite a quantidade: "))
print("O valor final é:", calc_valor(preco,qtd))