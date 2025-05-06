from typing import List


def converter_para_inteiros(telefones: List[str]) -> List[int]:
    """
    Converte uma lista de números de telefone armazenados como strings
    para inteiros.

    Args:
        telefones (List[str]): lista de números de telefone em formato str

    Returns:
        List[int]: lista de números de telefone como int

    Raises:
        ValueError: se algum elemento da lista não puder ser convertido
    """
    try:
        return [int(t) for t in telefones]
    except ValueError as err:
        # Repassa o erro para quem estiver chamando lidar
        raise ValueError(f"Número de telefone inválido encontrado: {err}") from err


def verificar_inteiros(valores: List[object]) -> bool:
    """
    Verifica se todos os elementos de uma lista são inteiros.

    Args:
        valores (List[object]): lista a ser verificada

    Returns:
        bool: True se todos forem int, False caso contrário
    """
    return all(isinstance(v, int) for v in valores)


# --- Demonstração rápida ---
if __name__ == "__main__":
    telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]

    # 1) Converte para inteiros
    telefones_int = converter_para_inteiros(telefones)

    # 2) Verifica se a conversão foi bem‑sucedida
    if verificar_inteiros(telefones_int):
        print("Todos os números foram convertidos corretamente!")
        print(telefones_int)
    else:
        print("Há números que ainda não são inteiros.")
