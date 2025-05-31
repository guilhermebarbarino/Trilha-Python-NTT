def menu() -> str:
    print("\n=== Gestão Financeira ===")
    print("1. Adicionar transação")
    print("2. Listar transações")
    print("3. Atualizar transação")
    print("4. Deletar transação")
    print("5. Sair")
    return input("Escolha uma opção: ").strip()