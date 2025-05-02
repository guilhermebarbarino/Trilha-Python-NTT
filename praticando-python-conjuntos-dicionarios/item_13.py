# Dicionário de vendas organizadas por categoria
vendas = {
    "Eletrônicos": [
        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000},
        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500}
    ],
    "Eletrodomésticos": [
        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000},
        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800}
    ],
    "Livros": [
        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50},
        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100}
    ]
}

# Exibe o total por categoria
print("Total de vendas por categoria:\n")

for categoria, lista_vendas in vendas.items():
    total_categoria = sum(item["quantidade"] * item["valor_unitario"] for item in lista_vendas)
    print(f"- {categoria}: R$ {total_categoria:.2f}")
