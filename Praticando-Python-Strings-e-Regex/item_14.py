entrada = input("Digite o nome completo e o ano de nascimento do paciente: ")

nome_completo, ano_nascimento = entrada.split(" - ")
primeiro_nome, sobrenome = nome_completo.split()

print(f"Primeiro Nome: {primeiro_nome}")
print(f"Sobrenome: {sobrenome}")
print(f"Ano de Nascimento: {ano_nascimento}")
