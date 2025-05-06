def obter_pares(numeros_str: str) -> list[int]:
    """
    Recebe uma string com números separados por espaço e
    devolve apenas os números pares, como lista de int.

    Args:
        numeros_str (str): ex. "1 2 3 4 5 6"

    Returns:
        list[int]: lista contendo apenas os números pares
    """
    # Converte cada item para inteiro
    numeros = map(int, numeros_str.split())

    # Usa filter() para manter somente os pares
    pares = filter(lambda x: x % 2 == 0, numeros)

    return list(pares)


if __name__ == "__main__":
    entrada = input("Digite os números separados por espaço: ").strip()
    pares = obter_pares(entrada)

    if pares:
        # Converte a lista de pares em string separados por espaço
        print("Números pares:", *pares)
    else:
        print("Nenhum número par encontrado.")
