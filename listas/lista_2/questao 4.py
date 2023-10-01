not1 = float(input("Digite sua primeira nota: "))
not2 = float(input("Digite sua segunda nota: "))

media = (not1 + not2) / 2

if media >= 6:
    print(f"Sua media é:",media ,"voce foi aprovado!")
else:
    print(f"Sua media é:",media ,"voce foi reprovado")