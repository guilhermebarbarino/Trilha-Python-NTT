def calcular_gorjeta():
    # Lê o valor da conta e converte vírgula em ponto, se houver
    valor_conta = float(
        input("Digite o valor da conta: ").strip().replace(",", ".")
    )

    # Lê a porcentagem de gorjeta e faz a mesma normalização
    porcentagem = float(
        input("Digite a porcentagem de gorjeta: ").strip().replace(",", ".")
    )

    # Calcula gorjeta e total
    gorjeta = valor_conta * (porcentagem / 100)
    total = valor_conta + gorjeta

    # Exibe resultados formatados
    print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")


if __name__ == "__main__":
    calcular_gorjeta()
