def calculadora(a: float, b: float, op: str) -> float:
    """
    Realiza a operação indicada por `op` sobre `a` e `b`.

    Args:
        a (float): primeiro número
        b (float): segundo número
        op (str): '+', '-', '*', ou '/'

    Returns:
        float: resultado da operação

    Raises:
        ValueError: operador inválido ou divisão por zero
    """
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else
             (_ for _ in ()).throw(ValueError("Divisão por zero não é permitida"))
    }

    if op not in operacoes:
        raise ValueError("Operador inválido. Use +, -, * ou /.")

    return operacoes[op](a, b)


# Bloco interativo
if __name__ == "__main__":
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        oper = input("Escolha a operação (| + | - | * | / |): ").strip()

        resultado = calculadora(num1, num2, oper)
        print(f"O resultado é: {resultado:g}")
    except ValueError as e:
        print(f"Erro: {e}")
