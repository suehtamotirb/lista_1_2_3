nota1 = float(input("Digite sua primera nota: "))
nota2 = float(input("Digite sua segunda nota: "))

med = (nota1 + nota2)/2

if med >= 9:
    print(f"Suas notas foram:", nota1, nota2,"sua media foi:", med,"você teve conceito A, Parabens você foi aprovado")
elif 9 > med >= 7.5:
    print(f"Suas notas foram:", nota1, nota2,"sua media foi:", med,"você teve conceito B, Parabens você foi aprovado")
elif 7.5 > med >= 6:
    print(f"Suas notas foram:", nota1, nota2,"sua media foi:", med,"você teve conceito C, Parabens você foi aprovado")
elif 6 > med >= 4:
    print(f"Suas notas foram:", nota1, nota2,"sua media foi:", med,"você teve conceito D, Infelizmente você foi reprovado")
else:
    print(f"Suas notas foram:", nota1, nota2,"sua media foi:", med,"você teve conceito E, Infelizmente você foi reprovado")