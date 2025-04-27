texto = input("Digite o texto a ser revisado: ")
palavra_antiga = input("Qual palavra deseja substituir? ")
palavra_nova = input("Qual a nova palavra? ")

texto_revisado = texto.replace(palavra_antiga, palavra_nova)

print("\nTexto revisado:")
print(texto_revisado)
