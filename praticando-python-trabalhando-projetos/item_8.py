import re

def encontrar_palavras_longas():
    texto = input("Digite um texto: ")

    # Extrai apenas sequências de letras (Unicode) como palavras
    palavras = re.findall(r"\b\w+\b", texto, flags=re.UNICODE)

    # Filtra aquelas com mais de 10 letras
    longas = [p for p in palavras if len(p) > 10]

    if longas:
        print("Palavras longas encontradas:", ", ".join(longas))
    else:
        print("Nenhuma palavra longa foi encontrada no texto.")


if __name__ == "__main__":
    encontrar_palavras_longas()
