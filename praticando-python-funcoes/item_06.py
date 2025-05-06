def saudacao(hora: int) -> str:
    """
    Retorna uma saudação apropriada com base na hora (0‑23).

    Args:
        hora (int): hora atual em formato 24 h

    Returns:
        str: saudação correspondente
    """
    if not 0 <= hora <= 23:
        raise ValueError("A hora deve estar entre 0 e 23.")
    if hora < 12:
        return "Bom dia!"
    elif hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"


# Uso interativo
if __name__ == "__main__":
    try:
        hora_atual = int(input("Digite a hora atual (0‑23): "))
        print(saudacao(hora_atual))
    except ValueError as e:
        print(f"Erro: {e}")
