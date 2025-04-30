# Lista de itens disponíveis na despensa
despensa = ['arroz', 'feijão', 'macarrão', 'sal', 'óleo', 'café']

# Solicita o item que o usuário quer verificar
item = input("Digite o item que você quer verificar: ").strip().lower()

# Verifica se o item está na despensa
if item in despensa:
    print(f"O item {item} já está na despensa.")
else:
    print(f"O item {item} precisa ser comprado.")
