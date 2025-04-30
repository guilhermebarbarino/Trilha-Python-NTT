# Solicita os dados dos alunos
entrada = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ")

# Divide a string de entrada em uma lista, removendo espaços extras
dados = [item.strip() for item in entrada.split(',')]

# Percorre os dados em grupos de 3 (Nome, Idade, Nota)
print()
for i in range(0, len(dados), 3):
    nome = dados[i]
    idade = dados[i + 1]
    nota = dados[i + 2]
    
    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}\n")
