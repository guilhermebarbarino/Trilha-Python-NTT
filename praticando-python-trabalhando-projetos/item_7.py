def contar_vogais():
    texto = input("Digite um texto: ")

    vogais = "aeiou"
    total = sum(1 for caractere in texto.lower() if caractere in vogais)

    print(f"Número de vogais: {total}")


if __name__ == "__main__":
    contar_vogais()
