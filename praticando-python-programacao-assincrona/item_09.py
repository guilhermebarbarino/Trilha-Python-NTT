import asyncio
from typing import Dict, List

pedidos: List[Dict] = [
    {"id": 101, "pagamento_aprovado": True,  "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True,  "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True,  "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]

async def processar_pedido(pedido: Dict) -> None:
    pid = pedido["id"]
    print(f"\n⏳ Processando pedido {pid}...")

    # 1️⃣ Verifica pagamento
    await asyncio.sleep(0.4)  # simula consulta a provedor de pagamentos
    if not pedido["pagamento_aprovado"]:
        print(f"❌ Pagamento NÃO aprovado para o pedido {pid}. Pedido cancelado.")
        return
    print(f"✅ Pagamento aprovado para o pedido {pid}.")

    # 2️⃣ Verifica estoque
    await asyncio.sleep(0.3)  # simula checagem de estoque
    if not pedido["estoque_disponivel"]:
        print(f"❌ Estoque indisponível para o pedido {pid}. Pedido cancelado.")
        return
    print(f"✅ Estoque confirmado para o pedido {pid}.")

    # 3️⃣ Confirma e envia
    await asyncio.sleep(0.2)  # simula preparação e expedição
    print(f"📦 Pedido {pid} confirmado e enviado para entrega!")

async def main() -> None:
    print("🚀 Iniciando processamento assíncrono dos pedidos...")
    # Seleciona os três primeiros pedidos para a simulação
    tarefas = [asyncio.create_task(processar_pedido(p)) for p in pedidos[:3]]
    await asyncio.gather(*tarefas)
    print("\n✅ Todos os pedidos foram processados!")

if __name__ == "__main__":
    asyncio.run(main())
