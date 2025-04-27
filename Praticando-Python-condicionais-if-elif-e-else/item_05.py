atividade_a = int(input("Digite o número de dias para a atividade A: "))
atividade_b = int(input("Digite o número de dias para a atividade B: "))
atividade_c = int(input("Digite o número de dias para a atividade C: "))

if atividade_a < 0 or atividade_b < 0 or atividade_c < 0:
    print("Erro: Valores inseridos são inválidos. Nenhum valor pode ser negativo.")
else:
    tempo_total = atividade_a + atividade_b + atividade_c
    print(f"Tempo total do projeto: {tempo_total} dias.")
