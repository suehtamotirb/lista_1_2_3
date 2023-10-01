A_est = int(input("Digite a quantidade atual de estoque: "))
M_est = int(input("Digite a quantidade maxima de estoque: "))
Mi_est = int(input("Digite a quantidade atual de estoque: "))

Q_media = (M_est + Mi_est)/2

if A_est >= Q_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")





