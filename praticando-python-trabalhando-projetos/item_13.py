def mostrar_menu():
    print("\n1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

def adicionar(tarefas):
    tarefa = input("Digite a tarefa: ").strip()
    if tarefa:
        tarefas.append(tarefa)
        print("Tarefa adicionada!")
    else:
        print("Nada foi adicionado (entrada vazia).")

def visualizar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas:")
        for i, t in enumerate(tarefas, start=1):
            print(f"{i}. {t}")

def remover(tarefas):
    if not tarefas:
        print("Erro: Nenhuma tarefa para remover.")
        return
    try:
        indice = int(input("Digite o número da tarefa a ser removida: "))
        if 1 <= indice <= len(tarefas):
            removida = tarefas.pop(indice - 1)
            print(f"Tarefa '{removida}' removida!")
        else:
            print("Erro: Número de tarefa inválido.")
    except ValueError:
        print("Erro: Entrada inválida! Digite um número.")

def main():
    tarefas = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            adicionar(tarefas)
        elif opcao == "2":
            visualizar(tarefas)
        elif opcao == "3":
            remover(tarefas)
        elif opcao == "4":
            print("Saindo do gerenciador de tarefas. Até mais!")
            break
        else:
            print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")

if __name__ == "__main__":
    main()
