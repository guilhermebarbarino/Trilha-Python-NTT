# Lista de classificação original
classificacao = ['Ana', 'Carlos', 'Pedro']

# Solicita o nome incorreto e o nome correto
nome_errado = input("Digite o nome incorreto: ").strip()
nome_correto = input("Digite o nome correto: ").strip()

# Verifica se o nome incorreto está na lista
if nome_errado in classificacao:
    # Encontra o índice e faz a substituição
    indice = classificacao.index(nome_errado)
    classificacao[indice] = nome_correto
    print(f"\nO nome {nome_errado} foi substituído por {nome_correto}.")
else:
    print(f"\nO nome {nome_errado} não foi encontrado na lista.")

# Exibe a lista atualizada
print("Lista atualizada:", classificacao)
