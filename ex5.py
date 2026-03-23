# O BG Futebol clube deseja aumentar o salário de seus jogadores, se o salário for até 1000 reais o aumento é de 20%, se for até 5000 reais é 10%, e mais que isso é 5%

nome = str(input("Digite o nome do jogador: "))
sal = float(input("Digite o salário atual: "))
print("Nome:", nome)
if sal <= 1000:
    print("Novo salário:", sal * 1.2)
elif sal <= 5000:
    print("Novo salário:", sal * 1.1) 
elif sal > 5000:
    print("Novo salário:", sal * 1.05)