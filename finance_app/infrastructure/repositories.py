from interface.repositories import TransacaoRepositoryInterface
from domain.entities import Transacao
from typing import List

class TransacaoRepository(TransacaoRepositoryInterface):
    def __init__(self):
        self._storage: List[Transacao] = []

    def adicionar(self, transacao: Transacao) -> None:
        self._storage.append(transacao)

    def listar(self) -> List[Transacao]:
        return list(self._storage)

    def atualizar(self, id: int, transacao: Transacao) -> bool:
        for index, t in enumerate(self._storage):
            if t.id == id:
                self._storage[index] = transacao
                return True
        return False

    def deletar(self, id: int) -> bool:
        for t in self._storage:
            if t.id == id:
                self._storage.remove(t)
                return True
        return False

    def existe(self, id: int) -> bool:
        return any(t.id == id for t in self._storage)