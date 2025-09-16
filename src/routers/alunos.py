from fastapi import APIRouter, HTTPException
from src.models import Aluno, AlunoUpdate
from src.database import alunos_db
import uuid
from datetime import datetime

router = APIRouter()


@router.post("/", response_model=Aluno)
async def criar_aluno(aluno: Aluno):
    aluno_id = str(uuid.uuid4())
    aluno.id = aluno_id
    aluno.data_criacao = datetime.now().isoformat()
    alunos_db[aluno_id] = aluno.dict()
    return aluno


@router.get("/", response_model=list[Aluno])
async def listar_alunos(ativo: bool = None):
    if ativo is not None:
        return [aluno for aluno in alunos_db.values() if aluno['ativo'] == ativo]
    return list(alunos_db.values())


@router.get("/{aluno_id}", response_model=Aluno)
async def buscar_aluno(aluno_id: str):
    if aluno_id not in alunos_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return alunos_db[aluno_id]


@router.put("/{aluno_id}", response_model=Aluno)
async def atualizar_aluno(aluno_id: str, aluno_update: AlunoUpdate):
    if aluno_id not in alunos_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    aluno_atual = alunos_db[aluno_id]
    update_data = aluno_update.dict(exclude_unset=True)
    aluno_atual.update(update_data)
    alunos_db[aluno_id] = aluno_atual
    return aluno_atual


@router.delete("/{aluno_id}")
async def deletar_aluno(aluno_id: str):
    if aluno_id not in alunos_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    del alunos_db[aluno_id]
    return {"message": "Aluno deletado com sucesso"}
