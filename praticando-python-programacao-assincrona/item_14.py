import asyncio
import random
import time
from typing import Dict, List

# ----------------------------- Dados do problema -----------------------------

jogos: List[Dict] = [
    {"id": 1, "times": "Flamengo vs Palmeiras"},
    {"id": 2, "times": "São Paulo vs Corinthians"},
    {"id": 3, "times": "Grêmio vs Internacional"},
]

RESULTADOS = ["Vitória do Time A", "Vitória do Time B", "Empate"]

# ------------------------------- Corrotinas -----------------------------------

async def revelar_resultado(jogo: Dict, futuro: asyncio.Future) -> None:
    """
    Aguarda entre 2 e 8 s e define o resultado aleatório no `futuro`.
    Quando o resultado é definido, imprime a mensagem de conclusão.
    """
    delay = random.randint(2, 8)
    await asyncio.sleep(delay)

    time_a, time_b = jogo["times"].split(" vs ")
    escolha = random.choice(RESULTADOS)

    if escolha == "Vitória do Time A":
        resultado = f"Vitória do {time_a}"
    elif escolha == "Vitória do Time B":
        resultado = f"Vitória do {time_b}"
    else:
        resultado = "Empate"

    futuro.set_result((resultado, delay))

    print(f"Aposta no jogo {jogo['id']} definida: {resultado} (após {delay}s).")


async def main() -> None:
    random.seed()  # garante aleatoriedade diferente a cada execução
    futuros: List[asyncio.Future] = []

    # 1) Registra todas as apostas imediatamente
    for jogo in jogos:
        futuro = asyncio.get_event_loop().create_future()
        futuros.append(futuro)
        print(
            f"Aposta no jogo {jogo['id']} ({jogo['times']}) registrada! "
            "Aguardando resultado..."
        )
        # dispara a corrotina que decidirá o resultado
        asyncio.create_task(revelar_resultado(jogo, futuro))

    # 2) Aguarda TODOS os resultados: quando cada futuro é resolvido,
    #    asyncio.gather libera a próxima linha.
    await asyncio.gather(*futuros)

    print("\nTodos os resultados foram revelados!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")
