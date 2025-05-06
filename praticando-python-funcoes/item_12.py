def gerar_calculadora_desconto(porcentagem: float):
    """
    Gera uma função que aplica um desconto fixo (porcentagem) a qualquer valor.

    Args:
        porcentagem (float): percentual de desconto (ex.: 10 para 10%)

    Returns:
        Callable[[float], float]: função que recebe o valor da compra e
        devolve o preço final com desconto aplicado.
    """
    fator = 1 - porcentagem / 100

    def aplicar_desconto(valor_compra: float) -> float:
        return round(valor_compra * fator, 2)  # duas casas decimais

    return aplicar_desconto


# --- Demonstração interativa ---
if __name__ == "__main__":
    desconto = float(input("Digite a porcentagem de desconto: "))
    valor = float(input("Digite o valor da compra: "))

    calcular_preco_final = gerar_calculadora_desconto(desconto)
    preco_final = calcular_preco_final(valor)

    print(f"Preço final com desconto: {preco_final}")
