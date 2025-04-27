titulo = input("Digite o título do livro: ")
letra_inicial = input("Digite a letra inicial para pesquisa: ")

palavras = titulo.split()
palavras_filtradas = [palavra for palavra in palavras if palavra.startswith(letra_inicial)]

print(palavras_filtradas)
