nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:  "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1+nota2+nota3)/3


if media >= 8:
    print("O seu conceito é 'A' ")

elif media >= 5:
    print("O seu conceito é 'B' ")
    
else:
    print("O seu conceito é 'C' ")
    
print("Sua média é:", media)    