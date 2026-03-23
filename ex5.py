nome = str(input("Digite o nome do jogador: "))
sal = float(input("Digite o salário atual: "))
print("Nome:", nome)
if sal <= 1000:
    print("Novo salário:", sal * 1.2)
elif sal <= 5000:
    print("Novo salário:", sal * 1.1) 
elif sal > 5000:
    print("Novo salário:", sal * 1.05)