# Criando um conjunto para armazenar os nomes sem repetições
convidados = set()

while True:
    nome = input("Digite o nome do convidado: ")

    if nome.lower() == 'sair':
        break

    convidados.add(nome.strip())

# Convertendo o conjunto para uma lista para organizar os nomes
lista_ordenada = sorted(convidados)

# Exibindo os convidados confirmados
print("\nConvidados confirmados:", ", ".join(lista_ordenada))
