i = 0
maiores = 0
idade = []
nome = []
while True:
    n = str(input("Digite o nome do usuário ('encerrar' para parar): "))
    if n == "encerrar":
        break
    nome.append(n)
    idd = int(input("Digite a idade do usuário: "))
    idade.append(idd)
    if idd >= 18:
        maiores += 1
    i += 1
print("Usuários cadastrados:", i)
print("Usuários com maioridade:", maiores)