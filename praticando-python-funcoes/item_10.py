def combinar_produtos_e_precos(produtos_str: str, precos_str: str) -> dict[str, float]:
    """
    Recebe duas strings (produtos e preços, separadas por vírgula),
    associa cada produto ao preço correspondente e devolve um dicionário.

    Args:
        produtos_str (str): ex. "maçã, banana, pera"
        precos_str (str): ex. "2.5, 1.2, 3.0"

    Returns:
        dict[str, float]: {"maçã": 2.5, "banana": 1.2, ...}

    Raises:
        ValueError: se a quantidade de produtos e preços não for igual.
    """
    produtos = [p.strip() for p in produtos_str.split(',')]
    precos = [float(v.strip()) for v in precos_str.split(',')]

    if len(produtos) != len(precos):
        raise ValueError("A lista de produtos deve ter a mesma quantidade de itens que a lista de preços.")

    return dict(zip(produtos, precos))


if __name__ == "__main__":
    try:
        produtos_input = input("Digite os produtos separados por vírgula: ")
        precos_input = input("Digite os preços separados por vírgula: ")

        estoque = combinar_produtos_e_precos(produtos_input, precos_input)

        for produto, preco in estoque.items():
            print(f"{produto}: {preco:g}")
    except ValueError as e:
        print(f"Erro: {e}")
