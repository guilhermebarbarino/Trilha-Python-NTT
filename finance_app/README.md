# 💰 Gestão Financeira Pessoal (CLI) — Python + Clean Architecture

Este projeto é uma aplicação de linha de comando desenvolvida em Python que simula uma gestão financeira pessoal. Ele foi criado com foco em **arquitetura limpa (Clean Architecture)** e **código limpo (Clean Code)**, utilizando interfaces com `Protocol`, tipagem forte e testes automatizados com cobertura total.

---

## 🎯 Objetivo

Permitir ao usuário:

- Adicionar transações com ID, descrição e valor
- Listar todas as transações
- Atualizar transações existentes
- Deletar transações
- Verificar se uma transação existe por ID

---

## 🧱 Estrutura de Arquitetura

Organizado em camadas para manter baixo acoplamento e alta coesão:

```
finance_app/
├── main.py                    # Ponto de entrada da aplicação
│
├── domain/                   # Entidades centrais do domínio
│   └── entities.py           # Classe Transacao
│
├── application/              # Regras de negócio e casos de uso
│   └── services.py           # TransacaoService
│
├── infrastructure/           # Implementações concretas (repositório em memória)
│   └── repositories.py       # TransacaoRepository
│
├── interface/                # Interfaces (Protocols) + menu CLI
│   ├── repositories.py       # Interface do repositório
│   ├── services.py           # Interface do serviço
│   └── menu.py               # Interface do usuário
│
├── tests/                    # Testes unitários automatizados
│   ├── test_transacao_service.py
│   └── test_transacao_extra.py
│
├── requirements.txt          # Dependências (pytest, coverage)
└── README.md                 # Este documento
```

---

## ⚙️ Como executar

### 1. Criar ambiente virtual
```bash
python -m venv venv
```

### 2. Ativar ambiente

- **Windows:**
```bash
venv\Scripts\activate
```

- **Linux/macOS:**
```bash
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar o programa
```bash
python main.py
```

---

## 🧪 Testes e Cobertura

### Rodar os testes:
```bash
pytest
```

### Rodar com cobertura:
```bash
coverage run -m pytest
coverage report -m
```

### Gerar relatório em HTML:
```bash
coverage html
# Depois abra: htmlcov/index.html
```

---

## ✅ Boas práticas aplicadas

- Clean Architecture
- Clean Code com nomes claros e responsabilidades únicas
- Interfaces com `Protocol`
- Uso do `@dataclass` para simplificação de entidades
- Testes unitários completos
- Alta cobertura com `coverage`

---

## 🔧 Melhorias futuras a fazer

- Persistência com banco de dados.
- Exportação/importação de dados (JSON, CSV).
- Interface gráfica - API REST.
- Deploy com Docker
- Integração contínua com GitHub Actions

---

