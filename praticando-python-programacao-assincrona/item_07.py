import asyncio
import math
from typing import Tuple, List

async def calcular_fatorial(n: int) -> Tuple[int, int]:
    """Simula um cálculo pesado do fatorial de n."""
    await asyncio.sleep(n * 0.1)        # tempo de “processamento” proporcional ao tamanho
    return n, math.factorial(n)

async def main(numeros: List[int]) -> None:
    # Cria e dispara todas as tarefas de uma vez
    tarefas = [asyncio.create_task(calcular_fatorial(n)) for n in numeros]

    for concluida in asyncio.as_completed(tarefas):
        n, f = await concluida
        print(f"Fatorial de {n} = {f}")

if __name__ == "__main__":
    # Lista em ordem aleatória, como no exemplo do enunciado
    numeros = [5, 3, 7, 4, 6]
    asyncio.run(main(numeros))
