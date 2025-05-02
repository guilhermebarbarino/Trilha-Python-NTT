# Recebendo os dois textos
texto1 = input("Texto 1: ").lower()
texto2 = input("Texto 2: ").lower()

# Convertendo os textos em conjuntos de palavras
palavras1 = set(texto1.split())
palavras2 = set(texto2.split())

# Encontrando a interseção (palavras em comum)
comum = palavras1 & palavras2

# Exibindo o resultado
print("\nPalavras em comum:", comum)
