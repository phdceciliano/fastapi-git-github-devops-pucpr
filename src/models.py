from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Aluno(BaseModel):
    id: Optional[str] = None
    nome: str
    idade: int
    plano: str
    ativo: bool = True
    data_criacao: Optional[str] = None

class Treino(BaseModel):
    id: Optional[str] = None
    aluno_id: str
    tipo: str
    exercicios: List[str]
    duracao_minutos: int
    data: Optional[str] = None

class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    plano: Optional[str] = None
    ativo: Optional[bool] = None

class TreinoUpdate(BaseModel):
    aluno_id: Optional[str] = None
    tipo: Optional[str] = None
    exercicios: Optional[List[str]] = None
    duracao_minutos: Optional[int] = None