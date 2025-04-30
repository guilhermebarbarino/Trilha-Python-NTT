# Entrada dos produtos do primeiro estoque
entrada1 = input("Produtos do estoque 1 (separados por vírgula): ")
# Entrada dos produtos do segundo estoque
entrada2 = input("Produtos do estoque 2 (separados por vírgula): ")

# Converte as entradas em tuplas, removendo espaços extras
estoque1 = tuple(produto.strip() for produto in entrada1.split(','))
estoque2 = tuple(produto.strip() for produto in entrada2.split(','))

# Combina os dois estoques
estoque_combinado = estoque1 + estoque2

# Exibe o relatório unificado
print("\nEstoque combinado:")
print(estoque_combinado)
