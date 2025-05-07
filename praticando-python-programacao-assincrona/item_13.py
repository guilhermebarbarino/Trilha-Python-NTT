import asyncio
import random
from datetime import datetime

VELOCIDADE_MB_S = 5                         # velocidade de download
QTD_ARQUIVOS    = 5                         # número de arquivos
TAMANHO_MIN_MB  = 10                        # tamanho mínimo (MB)
TAMANHO_MAX_MB  = 50                        # tamanho máximo (MB)

def timestamp(segundos: int) -> str:
    """Formata o tempo decorrido como [Xs]."""
    return f"[{segundos}s]"

async def baixar_arquivo(nome: str, tamanho: int, inicio: float) -> None:
    """Corrotina que faz o download 'virtual' do arquivo."""
    print(f"Iniciando download de {nome} (tamanho: {tamanho}MB)...")

    baixado = 0
    segundos_decorridos = 0

    while baixado < tamanho:
        # Espera um segundo “real” (simula tempo de rede/I/O)
        await asyncio.sleep(1)
        segundos_decorridos += 1
        baixado += VELOCIDADE_MB_S
        if baixado > tamanho:
            baixado = tamanho

        print(f"{timestamp(segundos_decorridos)} {nome}: {baixado}MB baixados")

    # Download concluído
    print(f"{nome} concluído!")

async def main() -> None:
    random.seed()  # garante tamanhos aleatórios diferentes a cada execução

    # Gera tamanhos aleatórios e nomes de arquivos
    arquivos = [
        (f"arquivo_{i}.txt", random.randint(TAMANHO_MIN_MB, TAMANHO_MAX_MB))
        for i in range(1, QTD_ARQUIVOS + 1)
    ]

    # Dispara downloads em paralelo
    tarefas = [
        asyncio.create_task(baixar_arquivo(nome, tamanho, asyncio.get_event_loop().time()))
        for nome, tamanho in arquivos
    ]

    # Aguarda todos terminarem
    await asyncio.gather(*tarefas)
    print("\nTodos os downloads foram finalizados!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nDownload interrompido pelo usuário.")
