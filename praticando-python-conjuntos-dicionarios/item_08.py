# Conjuntos de tarefas das equipes
equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

# União das tarefas
tarefas_consolidadas = equipe_a | equipe_b

# Exibe a lista antes da remoção
print("Lista consolidada de tarefas:", tarefas_consolidadas)

# Solicita ao usuário a tarefa a ser removida
tarefa_remover = input("Informe a tarefa que deseja remover: ").lower().strip()

# Remove a tarefa, se existir
tarefas_consolidadas = {tarefa for tarefa in tarefas_consolidadas if tarefa.lower() != tarefa_remover}

# Exibe o resultado final
print("\nTarefas finais:", tarefas_consolidadas)
