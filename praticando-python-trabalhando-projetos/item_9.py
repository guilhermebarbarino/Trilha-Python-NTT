import secrets
import string

def gerar_senha(tamanho=12):
    if tamanho < 4:
        raise ValueError("Tamanho mínimo da senha é 4.")

    # Conjuntos de caracteres
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    digitos    = string.digits
    especiais  = "!@#$%^&*()-_=+[]{};:,<.>/?"

    # Garante pelo menos um de cada categoria
    senha = [
        secrets.choice(maiusculas),
        secrets.choice(minusculas),
        secrets.choice(digitos),
        secrets.choice(especiais)
    ]

    # Preenche o restante aleatoriamente com a junção de todos os conjuntos
    todos = maiusculas + minusculas + digitos + especiais
    senha += [secrets.choice(todos) for _ in range(tamanho - 4)]

    # Embaralha para não deixar os 4 primeiros previsíveis
    secrets.SystemRandom().shuffle(senha)

    return "".join(senha)

if __name__ == "__main__":
    senha = gerar_senha(12)
    print("Senha gerada:", senha)
