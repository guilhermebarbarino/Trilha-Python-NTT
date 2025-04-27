hora_atual = int(input("Digite a hora atual (formato 24h exemplo -> 21): "))

if 8 <= hora_atual <= 18:
    print("Acesso permitido. Bem-vindo ao escritório!")
else:
    print("Acesso negado. Fora do horário permitido.")
