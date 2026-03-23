# Faça um programa para pagamento de comissão de vendedores, com comissão de 5%, peça o ID do vendedor, o código da peça, o preço unitário e a quantidade vendida. Apresente os dois primeiros e a comissão.

idVend = int(input("Digite o ID do vendedor: "))
codPeca = int(input("Digite o código da peça: "))
precoUni = float(input("Digite o preço unitário: "))
qtd = int(input("Digite a quantidade vendida: "))
print("ID do vendedor:", idVend)
print("Código da peça:", codPeca)
print("Comissão:", qtd * precoUni * 0.05)