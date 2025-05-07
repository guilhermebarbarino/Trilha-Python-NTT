import asyncio
from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    vip: bool
    notificacoes_ativadas: bool

    async def enviar_notificacao(self) -> None:
        """Envia a notificação adequada ou informa que nada foi enviado."""
        # Pequeno delay para simular tempo de envio
        await asyncio.sleep(0.1)

        if not self.notificacoes_ativadas:
            print(f"{self.nome} desativou as notificações. Nada foi enviado.")
            return

        if self.vip:
            print(f"Notificação VIP para {self.nome} enviada!")
        else:
            print(f"Notificação normal para {self.nome} enviada!")

async def processar_notificacoes(usuarios):
    print("Enviando notificações...")

    # 1️⃣ Prioriza VIPs, 2️⃣ depois os demais
    usuarios_ordenados = sorted(usuarios, key=lambda u: not u.vip)

    # Envia notificações uma a uma (poderia usar gather se quisesse paralelizar)
    for usuario in usuarios_ordenados:
        await usuario.enviar_notificacao()

    print("Todas as notificações foram processadas!")

if __name__ == "__main__":
    usuarios = [
        Usuario(nome="Ana",   vip=True,  notificacoes_ativadas=True),
        Usuario(nome="João",  vip=False, notificacoes_ativadas=True),
        Usuario(nome="Carla", vip=False, notificacoes_ativadas=False),
    ]
    asyncio.run(processar_notificacoes(usuarios))
