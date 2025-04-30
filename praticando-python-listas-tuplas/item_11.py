# Solicita os pedidos feitos, separados por vírgula
entrada = input("Pedidos feitos (separados por vírgula): ")

# Converte a entrada em uma lista, removendo espaços extras
pedidos = [item.strip() for item in entrada.split(',')]

# Remove o último item da lista
if pedidos:
    removido = pedidos.pop()
    print(f"\nO pedido '{removido}' foi removido por engano.")
else:
    print("\nNenhum pedido foi encontrado.")

# Exibe a lista final de pedidos
print("Pedidos finais:", pedidos)
