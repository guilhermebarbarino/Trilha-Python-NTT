# Dicionário com os participantes e suas idades
participantes = {
    "Mariana": 25,
    "Carlos": 32,
    "Beatriz": 28,
    "Rafael": 35
}

# Obtendo os nomes e as idades separadamente
nomes = ", ".join(participantes.keys())
idades = ", ".join(str(idade) for idade in participantes.values())

# Exibindo os resultados
print("Nomes dos participantes:", nomes)
print("Idades dos participantes:", idades)

print("\nParticipantes e suas idades:")
for nome, idade in participantes.items():
    print(f"- {nome}: {idade} anos")
