from fastapi import APIRouter, HTTPException
from src.models import Treino, TreinoUpdate
from src.database import treinos_db, alunos_db
import uuid
from datetime import datetime

router = APIRouter()


@router.post("/", response_model=Treino)
async def criar_treino(treino: Treino):
    if treino.aluno_id not in alunos_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    treino_id = str(uuid.uuid4())
    treino.id = treino_id
    treino.data = datetime.now().isoformat()
    treinos_db[treino_id] = treino.model_dump()
    return treino


@router.get("/", response_model=list[Treino])
async def listar_treinos(aluno_id: str = None):
    if aluno_id:
        if aluno_id not in alunos_db:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        return [treino for treino in treinos_db.values()
                if treino['aluno_id'] == aluno_id]
    return list(treinos_db.values())


@router.get("/{treino_id}", response_model=Treino)
async def buscar_treino(treino_id: str):
    if treino_id not in treinos_db:
        raise HTTPException(status_code=404, detail="Treino não encontrado")
    return treinos_db[treino_id]


@router.put("/{treino_id}", response_model=Treino)
async def atualizar_treino(treino_id: str, treino_update: TreinoUpdate):
    if treino_id not in treinos_db:
        raise HTTPException(
            status_code=404,
            detail="Treino não encontrado"
        )

    treino_atual = treinos_db[treino_id]
    update_data = treino_update.model_dump(exclude_unset=True)

    if 'aluno_id' in update_data and update_data['aluno_id'] not in alunos_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    treino_atual.update(update_data)
    treinos_db[treino_id] = treino_atual
    return treino_atual


@router.delete("/{treino_id}")
async def deletar_treino(treino_id: str):
    if treino_id not in treinos_db:
        raise HTTPException(status_code=404, detail="Treino não encontrado")

    del treinos_db[treino_id]
    return {"message": "Treino deletado com sucesso"}
