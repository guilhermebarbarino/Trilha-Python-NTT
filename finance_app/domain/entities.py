from dataclasses import dataclass

@dataclass
class Transacao:
    id: int
    descricao: str
    valor: float

    def __repr__(self) -> str:
        return f"Transacao(id={self.id}, descricao='{self.descricao}', valor={self.valor:.2f})"