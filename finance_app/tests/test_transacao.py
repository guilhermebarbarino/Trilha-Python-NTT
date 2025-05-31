import pytest
from application.services import TransacaoService
from infrastructure.repositories import TransacaoRepository
from domain.entities import Transacao

@pytest.fixture
def setup_service():
    repo = TransacaoRepository()
    service = TransacaoService(repo)
    return service

def test_listar_vazio(setup_service):
    service = setup_service
    assert service.listar_transacoes() == []

def test_atualizar_transacao_inexistente(setup_service):
    service = setup_service
    atualizado = service.atualizar_transacao(999, "Teste", 10.0)
    assert atualizado is False

def test_deletar_transacao_inexistente(setup_service):
    service = setup_service
    deletado = service.deletar_transacao(999)
    assert deletado is False

def test_repr_transacao():
    t = Transacao(id=1, descricao="Teste", valor=10.5)
    assert repr(t) == "Transacao(id=1, descricao='Teste', valor=10.50)"

def test_criar_e_listar_transacao():
    repo = TransacaoRepository()
    service = TransacaoService(repo)

    service.criar_transacao(1, "Salário", 2500.00)
    transacoes = service.listar_transacoes()

    assert len(transacoes) == 1
    assert transacoes[0].descricao == "Salário"

def test_atualizar_transacao():
    repo = TransacaoRepository()
    service = TransacaoService(repo)

    service.criar_transacao(1, "Freela", 1500.00)
    atualizou = service.atualizar_transacao(1, "Freelancer", 2000.00)

    assert atualizou
    assert repo.listar()[0].descricao == "Freelancer"

def test_deletar_transacao():
    repo = TransacaoRepository()
    service = TransacaoService(repo)

    service.criar_transacao(1, "Investimento", 1000.00)
    deletado = service.deletar_transacao(1)

    assert deletado
    assert len(service.listar_transacoes()) == 0

def test_existe_transacao():
    repo = TransacaoRepository()
    service = TransacaoService(repo)

    service.criar_transacao(1, "Renda Extra", 300.00)
    assert service.existe_transacao(1) is True
    assert service.existe_transacao(2) is False