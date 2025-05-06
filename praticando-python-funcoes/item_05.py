def contar_caracteres(palavra: str) -> int:
    """
    Retorna a quantidade de caracteres de uma palavra.

    Args:
        palavra (str): palavra cujo tamanho será contado

    Returns:
        int: número de caracteres
    """
    return len(palavra)


if __name__ == "__main__":
    palavra = input("Digite uma palavra: ").strip()
    tamanho = contar_caracteres(palavra)
    print(f"Essa palavra tem {tamanho} caracteres.")
