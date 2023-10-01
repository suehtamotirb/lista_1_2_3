ident = float(input("Digite o seu numero de conta: "))
saldo = float(input("Digite o seu numero do seu saldo: "))
debito = float(input("Digite o seu numero do seu debito: "))
credito = float(input("Digite o seu numero de credito: "))

S_atual = (saldo - debito) + credito

if S_atual >= 0 :
    print(f"Seu saldo atual é:",S_atual,"Seu saldo é positivo")
else:
    print(f"Seu saldo atual é:",S_atual,"seu saldo é negativa")