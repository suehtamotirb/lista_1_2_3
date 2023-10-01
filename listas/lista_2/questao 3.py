quant = int(input("Quantas maças deseja comprar? a partir de 12 tem desconto! "))

if quant < 12:
    soma = quant * 1.30
    print(f"R$:",soma)
else:
    soma = quant
    print(f"R$:",soma)