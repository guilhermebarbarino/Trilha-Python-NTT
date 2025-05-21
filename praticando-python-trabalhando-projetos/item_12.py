try:
    # Entradas
    num1 = float(input("Digite o primeiro número: "))
    op   = input("Escolha a operação (+, -, *, /): ").strip()
    num2 = float(input("Digite o segundo número: "))

    # Cálculo
    if op == "+":
        resultado = num1 + num2
    elif op == "-":
        resultado = num1 - num2
    elif op == "*":
        resultado = num1 * num2
    elif op == "/":
        if num2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        resultado = num1 / num2
    else:
        raise ValueError("Opção inválida")

    print("Resultado:", resultado)

except ValueError as e:
    print("Erro:", e)
except ZeroDivisionError as e:
    print("Erro:", e)
