import re

descricao = input("Digite a descrição da receita: ")

numero_receita = re.search(r'\d+', descricao)

if numero_receita:
    print(f"O número da receita é: {numero_receita.group()}")
else:
    print("Nenhum número de receita encontrado.")
