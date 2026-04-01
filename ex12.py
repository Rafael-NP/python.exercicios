nota = []
i = 0
while True:
    valor = float(input("Digite a nota (-1 para parar): "))   
    if valor == -1:
        break   
    nota.append(valor)
    i += 1
media = sum(nota) / i
maior = max(nota)
menor = min(nota)
print("Média:", media)
print("Maior nota:", maior)
print("Menor nota:", menor)