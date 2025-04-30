# Lista inicial de convidados
convidados = ['Ana', 'Pedro', 'Carlos']

# Mostra a lista atual
print("Lista atual de convidados:", convidados)

# Solicita o nome do novo convidado
novo_convidado = input("Digite o nome do novo convidado: ").strip()

# Solicita a posição onde o novo convidado será inserido
posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))

# Insere o novo convidado na posição escolhida
convidados.insert(posicao, novo_convidado)

# Exibe a lista atualizada
print("\nLista atualizada de convidados:", convidados)
