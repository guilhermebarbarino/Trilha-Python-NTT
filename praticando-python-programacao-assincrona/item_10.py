import asyncio
from typing import Dict, List

# ----- Dados iniciais --------------------------------------------------------
cursos: Dict[str, Dict] = {
    "Python Avançado":     {"vagas": 2, "inscritos": []},
    "Java para Iniciantes": {"vagas": 1, "inscritos": []},
    "Machine Learning":    {"vagas": 0, "inscritos": []},
}

alunos: List[Dict] = [
    {"nome": "Alice",   "curso": "Python Avançado"},
    {"nome": "Bruno",   "curso": "Python Avançado"},
    {"nome": "Carlos",  "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},
    {"nome": "Alice",   "curso": "Python Avançado"},  # inscrição duplicada
]

# ----- Funções ---------------------------------------------------------------
async def inscrever(aluno: Dict, locks: Dict[str, asyncio.Lock]) -> None:
    """Tenta inscrever um aluno no curso desejado, seguindo todas as regras."""
    nome, curso = aluno["nome"], aluno["curso"]

    print(f"\nInscrevendo {nome} no curso {curso}...")

    # Pequeno atraso para simular I/O (DB, API etc.) e liberar o loop
    await asyncio.sleep(0.1)

    async with locks[curso]:                       # seção crítica por curso
        dados_curso = cursos[curso]

        # Regra 1: não permitir duplicidade
        if nome in dados_curso["inscritos"]:
            print(f"{nome} já está inscrita no curso {curso}! Inscrição rejeitada.")
            return

        # Regra 2: verificar vagas
        if dados_curso["vagas"] > 0:
            dados_curso["vagas"] -= 1
            dados_curso["inscritos"].append(nome)
            print(f"Inscrição confirmada para {nome} no curso {curso}!")
        else:
            print(f"Turma lotada! {nome} não pôde se inscrever no curso {curso}.")

async def main() -> None:
    print("Processando inscrições...\n")

    # Um lock por curso garante consistência ao alterar vagas/inscritos
    locks = {curso: asyncio.Lock() for curso in cursos}

    # Dispara todas as inscrições em paralelo
    tarefas = [asyncio.create_task(inscrever(aluno, locks)) for aluno in alunos]
    await asyncio.gather(*tarefas)

    print("\nTodas as inscrições foram processadas!")

# ----- Execução --------------------------------------------------------------
if __name__ == "__main__":
    asyncio.run(main())
