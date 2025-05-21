try:
    valor = int(input("Digite o valor do saque: ").strip())

    if valor % 2 != 0 or valor <= 0:
        raise ValueError("O valor deve ser múltiplo de 2.")

    cedulas = [100, 50, 20, 10, 5, 2]
    print("\nCédulas entregues:")
    for c in cedulas:
        qtd, valor = divmod(valor, c)
        if qtd:
            print(f"{qtd} de R$ {c}")

except ValueError as e:
    print(f"Erro: {e}")
