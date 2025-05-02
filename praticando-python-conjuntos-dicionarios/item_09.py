# Inicializa o dicionário de produtos
estoque = {}

# Loop para cadastrar 3 produtos
for i in range(3):
    nome = input("Digite o nome do produto: ").strip().title()
    quantidade = int(input("Digite a quantidade: "))
    estoque[nome] = quantidade

# Exibe o dicionário final
print("\nDicionário de produtos:", estoque)
