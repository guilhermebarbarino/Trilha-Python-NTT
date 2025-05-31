from infrastructure.repositories import TransacaoRepository
from application.services import TransacaoService
from interface.menu import menu

def main():
    repo = TransacaoRepository()
    service = TransacaoService(repo)

    while True:
        opcao = menu()

        if opcao == "1":
            id_ = int(input("ID da transação: "))
            desc = input("Descrição: ")
            valor = float(input("Valor: "))
            service.criar_transacao(id_, desc, valor)
            print("✔ Transação adicionada!")

        elif opcao == "2":
            lst = service.listar_transacoes()
            if not lst:
                print("⚠ Nenhuma transação cadastrada.")
            else:
                for t in lst:
                    print(f"- {t}")

        elif opcao == "3":
            id_ = int(input("ID a atualizar: "))
            if not service.existe_transacao(id_):
                print("❌ ID não encontrado.")
                continue

            desc = input("Nova descrição: ")
            valor = float(input("Novo valor: "))
            service.atualizar_transacao(id_, desc, valor)
            print("✔ Atualizado com sucesso!")

        elif opcao == "4":
            id_ = int(input("ID a deletar: "))
            if service.deletar_transacao(id_):
                print("✔ Deletado com sucesso!")
            else:
                print("❌ ID não encontrado.")

        elif opcao == "5":
            print("👋 Até mais!")
            break

        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    main()