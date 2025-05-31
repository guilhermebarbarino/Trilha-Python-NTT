from domain.entities import Transacao
from interface.repositories import TransacaoRepositoryInterface
from interface.services import TransacaoServiceInterface
from typing import List

class TransacaoService(TransacaoServiceInterface):
    def __init__(self, repository: TransacaoRepositoryInterface):
        self._repo = repository

    def criar_transacao(self, id: int, descricao: str, valor: float) -> None:
        transacao = Transacao(id, descricao, valor)
        self._repo.adicionar(transacao)

    def listar_transacoes(self) -> List[Transacao]:
        return self._repo.listar()

    def atualizar_transacao(self, id: int, descricao: str, valor: float) -> bool:
        transacao = Transacao(id, descricao, valor)
        return self._repo.atualizar(id, transacao)

    def deletar_transacao(self, id: int) -> bool:
        return self._repo.deletar(id)

    def existe_transacao(self, id: int) -> bool:
        return self._repo.existe(id)