macas = int(input("Digite o número de vendas de maçãs: "))
bananas = int(input("Digite o número de vendas de bananas: "))

if macas > bananas:
    print("Maçãs tiveram maior venda!")
elif bananas > macas:
    print("Bananas tiveram maior venda!")
else:
    print("Houve um empate nas vendas!")
