import asyncio
import random

async def download() -> None:
    print("Iniciando download...")
    await asyncio.sleep(random.uniform(1.5, 3.0))   # simula tempo de download
    print("Download concluído!")

async def analise_dados() -> None:
    print("Iniciando análise de dados...")
    await asyncio.sleep(random.uniform(2.0, 4.0))   # simula tempo de análise
    print("Análise de dados concluída!")

async def main() -> None:
    await asyncio.gather(download(), analise_dados())

if __name__ == "__main__":
    asyncio.run(main())
