# Solicita as notas dos alunos separadas por vírgula
entrada = input("Digite as notas dos alunos separadas por vírgula: ")

# Converte a entrada em uma lista de números (float), removendo espaços extras
notas = [float(nota.strip()) for nota in entrada.split(',')]

# Calcula a média das notas
media = sum(notas) / len(notas) if notas else 0

# Exibe a média final da turma com duas casas decimais
print(f"\nMédia final da turma: {media:.2f}")
