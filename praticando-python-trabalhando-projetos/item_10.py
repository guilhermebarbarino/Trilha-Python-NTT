import random
import unicodedata

OPCOES = {"pedra", "papel", "tesoura"}


def normalizar(texto: str) -> str:
    """Remove acentos, deixa em minúsculas e tira espaços extras."""
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto.strip().lower()


def resultado(usuario: str, computador: str) -> str:
    if usuario == computador:
        return "Empate!"
    vence = {
        ("pedra", "tesoura"),
        ("tesoura", "papel"),
        ("papel", "pedra"),
    }
    return "Você venceu!" if (usuario, computador) in vence else "Você perdeu!"


def jogar():
    usuario = normalizar(
        input("Escolha: pedra, papel ou tesoura? ")
    )

    if usuario not in OPCOES:
        print("Entrada inválida. Tente novamente com pedra, papel ou tesoura.")
        return

    computador = random.choice(list(OPCOES))
    print(f"Computador escolheu: {computador}")
    print(resultado(usuario, computador))


if __name__ == "__main__":
    jogar()
