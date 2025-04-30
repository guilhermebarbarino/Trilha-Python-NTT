# Lista para armazenar os nomes dos voluntários
voluntarios = []

while True:
    nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ").strip()
    if nome.lower() == 'sair':
        break
    voluntarios.append(nome)

# Exibe a lista completa de voluntários registrados
print("Voluntários registrados:", voluntarios)
