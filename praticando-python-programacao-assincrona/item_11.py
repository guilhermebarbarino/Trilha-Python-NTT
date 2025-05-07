import asyncio
from typing import List

async def tarefa(idx: int, duracao: int, status: List[str]) -> None:
    """Simula uma tarefa que dura 'duracao' s."""
    await asyncio.sleep(duracao)           # processamento “pesado”
    status[idx] = "Finalizado"             # marca como concluída
    print(f"Tarefa {idx + 1} finalizada!")

async def main() -> None:
    status = ["Em andamento"] * 3          # status inicial das 3 tarefas

    # Cria tarefas assíncronas para durações de 3, 5 e 7 s
    duracoes = [3, 5, 7]
    tarefas = [asyncio.create_task(tarefa(i, d, status)) for i, d in enumerate(duracoes)]

    # Loop de monitoramento: roda até que todas estejam finalizadas
    while "Em andamento" in status:
        print(f"Status das tarefas: {status}")
        await asyncio.sleep(1)             # verifica a cada segundo

    # Garante que todas as tarefas já terminaram (boa prática)
    await asyncio.gather(*tarefas)

if __name__ == "__main__":
    asyncio.run(main())
