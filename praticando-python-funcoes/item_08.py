def somar_vendas(linha_valores: str) -> float:
    """
    Recebe uma string com valores numéricos separados por espaço
    e devolve a soma total.

    Args:
        linha_valores (str): ex. "100 250 300"

    Returns:
        float: total das vendas
    """
    try:
        valores = [float(v) for v in linha_valores.split()]
        return sum(valores)
    except ValueError as err:
        raise ValueError(f"Entrada inválida: {err}") from err


if __name__ == "__main__":
    entrada = input("Digite os valores das vendas: ").strip()
    try:
        total = somar_vendas(entrada)
        print(f"O total de vendas foi: {total:g}")
    except ValueError as e:
        print(f"Erro: {e}")
