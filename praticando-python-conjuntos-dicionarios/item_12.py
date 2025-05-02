# Dicionário com os workshops e os participantes
participantes = {
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"},
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"}
}

# Exibe a lista original
print("Lista original de participantes:")
for workshop, nomes in participantes.items():
    print(f"{workshop}: {nomes}")

# Solicita o nome do participante a ser removido
remover = input("\nNome do participante a ser removido: ").strip()

# Procura e remove o participante
for nomes in participantes.values():
    nomes.discard(remover)

# Exibe a lista atualizada
print("\nLista atualizada de participantes:")
for workshop, nomes in participantes.items():
    print(f"{workshop}: {nomes}")
