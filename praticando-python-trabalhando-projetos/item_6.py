def validar_cpf():
    cpf = input("Digite seu CPF: ").strip()

    # Verifica se contém apenas números
    if not cpf.isdigit():
        print("Erro: O CPF deve conter apenas números.")
        return

    # Verifica se tem exatamente 11 dígitos
    if len(cpf) != 11:
        print("Erro: O CPF deve ter exatamente 11 dígitos.")
        return

    print("CPF válido.")


if __name__ == "__main__":
    validar_cpf()
