from typing import Protocol, List
from domain.entities import Transacao

class TransacaoServiceInterface(Protocol):
    def criar_transacao(self, id: int, descricao: str, valor: float) -> None:
        ...

    def listar_transacoes(self) -> List[Transacao]:
        ...

    def atualizar_transacao(self, id: int, descricao: str, valor: float) -> bool:
        ...

    def deletar_transacao(self, id: int) -> bool:
        ...

    def existe_transacao(self, id: int) -> bool:
        ...