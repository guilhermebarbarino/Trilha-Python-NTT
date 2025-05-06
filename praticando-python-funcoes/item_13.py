def soma_recursiva(n: int) -> int:
    """
    Soma todos os inteiros de 1 até n (inclusivo) usando recursão.

    Args:
        n (int): número limite

    Returns:
        int: soma de 1 … n

    Raises:
        ValueError: se n < 1
    """
    if n < 1:
        raise ValueError("n deve ser um inteiro maior ou igual a 1.")
    if n == 1:                 # caso base
        return 1
    return n + soma_recursiva(n - 1)   # passo recursivo


# Demonstração rápida
if __name__ == "__main__":
    try:
        numero = int(input("Digite um número: "))
        resultado = soma_recursiva(numero)
        print(f"A soma de 1 a {numero} é: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")
