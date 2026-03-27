senha = "Roberta@"
i = 1
while i < 4:
    senhaDig = str(input("Digite sua senha: "))
    if senhaDig == senha:
        print("Acesso permitido.")
    elif i >= 3:
        print("Conta Bloqueada.")
    else:
        print("Senha errada, tente novamente.")
    i+=1