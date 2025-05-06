def calcular_idade(ano_nascimento: int, ano_atual: int) -> int:
    """
    Calcula a idade a partir do ano de nascimento e do ano atual.

    Args:
        ano_nascimento (int): ano em que a pessoa nasceu
        ano_atual (int): ano de referência para o cálculo

    Returns:
        int: idade em anos

    Levanta:
        ValueError: se o ano de nascimento for maior que o ano atual
    """
    if ano_nascimento > ano_atual:
        raise ValueError("O ano de nascimento não pode ser maior que o ano atual.")
    return ano_atual - ano_nascimento


if __name__ == "__main__":
    try:
        ano_nasc = int(input("Digite o ano de nascimento: "))
        ano_atual = int(input("Digite o ano atual: "))
        idade = calcular_idade(ano_nasc, ano_atual)
        print(f"A idade é {idade} anos.")
    except ValueError as e:
        print(f"Erro: {e}")
