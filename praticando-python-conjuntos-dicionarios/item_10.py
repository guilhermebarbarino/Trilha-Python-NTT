# Estoque inicial
estoque = {
    "Caderno universitário": 50,
    "Caneta azul": 120,
    "Borracha branca": 30
}

# Exibe o estoque atual
print("Estoque atual:", estoque)

# Solicita o nome do produto a ser atualizado
produto = input("\nNome do produto a ser atualizado: ").strip()

# Verifica se o produto existe no estoque
if produto in estoque:
    nova_quantidade = int(input("Nova quantidade: "))
    estoque[produto] = nova_quantidade
    print("\nEstoque atualizado:", estoque)
else:
    print("\nProduto não encontrado no estoque.")
