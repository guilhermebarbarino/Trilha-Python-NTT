import asyncio
import random
from datetime import datetime

TEMPERATURAS   = list(range(18, 30))               # °C realistas
UMIDADES       = list(range(45, 75))               # %
QUALIDADES_AR  = ["Boa", "Regular", "Ruim"]        # estados qualitativos

def timestamp() -> str:
    """Instante em segundos desde o início da execução."""
    agora = datetime.now()
    return f"[{(agora - START).seconds}s]"

async def sensor_temperatura(intervalo: int = 2) -> None:
    while True:
        await asyncio.sleep(intervalo)
        temp = random.choice(TEMPERATURAS)
        print(f"{timestamp()} Temperatura: {temp}°C")

async def sensor_umidade(intervalo: int = 3) -> None:
    while True:
        await asyncio.sleep(intervalo)
        umidade = random.choice(UMIDADES)
        print(f"{timestamp()} Umidade: {umidade}%")

async def sensor_qualidade_ar(intervalo: int = 5) -> None:
    while True:
        await asyncio.sleep(intervalo)
        qualidade = random.choice(QUALIDADES_AR)
        print(f"{timestamp()} Qualidade do ar: {qualidade}")

async def main() -> None:
    await asyncio.gather(
        sensor_temperatura(),
        sensor_umidade(),
        sensor_qualidade_ar(),
    )

if __name__ == "__main__":
    START = datetime.now()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado pelo usuário.")
