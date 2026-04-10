def maioridade(a):
    if a >= 18:
        maior = "Maior de idade."
    else:
        maior = "Menor de idade."
    return maior
pergunta = int(input("Digite a idade: "))
print(maioridade(pergunta))