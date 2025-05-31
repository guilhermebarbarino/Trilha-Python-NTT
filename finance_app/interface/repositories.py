from typing import Protocol
from domain.entities import Transacao
from typing import List

class TransacaoRepositoryInterface(Protocol):
    def adicionar(self, transacao: Transacao) -> None:
        ...

    def listar(self) -> List[Transacao]:
        ...

    def atualizar(self, id: int, transacao: Transacao) -> bool:
        ...

    def deletar(self, id: int) -> bool:
        ...

    def existe(self, id: int) -> bool:
        ...