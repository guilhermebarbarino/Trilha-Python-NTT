nome = input("Digite o nome do cliente para validação: ")

if nome.isalpha() and nome[0].isupper():
    print("Nome válido!")
else:
    print("Nome inválido!")
