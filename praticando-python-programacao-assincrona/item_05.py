import asyncio

async def temporizador(duracao: int = 3) -> None:
    """Exibe mensagem inicial, aguarda 'duracao' s e exibe mensagem final."""
    print("Iniciando temporizador...")
    await asyncio.sleep(duracao)           # espera sem bloquear o loop
    print(f"Tempo finalizado após {duracao} segundos!")

if __name__ == "__main__":
    asyncio.run(temporizador())
