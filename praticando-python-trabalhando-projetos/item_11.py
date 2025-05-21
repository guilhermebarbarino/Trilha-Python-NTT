import random

def jogo_adivinhacao():
    """Jogo de adivinhação: o computador escolhe um número de 1 a 100
    e o usuário tenta acertá-lo. Lança ValueError em entradas inválidas."""
    
    numero_secreto = random.randint(1, 100)

    while True:
        try:
            entrada = input("Tente adivinhar o número (1-100): ").strip()
            palpite = int(entrada)  # ValueError se não for número

            # Verifica se está no intervalo permitido
            if not 1 <= palpite <= 100:
                raise ValueError("Número fora do intervalo!")

            # Compara palpite com o número secreto
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente:")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente:")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto}.")
                break

        except ValueError as err:
            # Captura tanto conversão inválida quanto número fora do intervalo
            print(f"Entrada inválida: {err} Digite um número entre 1 e 100.")

if __name__ == "__main__":
    jogo_adivinhacao()
